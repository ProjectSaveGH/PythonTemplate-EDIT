import sys
import time
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError, StopApplication

class Buffer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.buffer = [[' ' for _ in range(width)] for _ in range(height)]
        self.colors = [[0 for _ in range(width)] for _ in range(height)]
        self.attributes = [[0 for _ in range(width)] for _ in range(height)]

    def print_at(self, text, x, y, colour=7, attr=0):
        for i, char in enumerate(text):
            if 0 <= x + i < self.width and 0 <= y < self.height:
                self.buffer[y][x + i] = char
                self.colors[y][x + i] = colour
                self.attributes[y][x + i] = attr

    def fill_rect(self, x1, y1, x2, y2, char=' ', colour=7, attr=0):
        for y in range(max(0, y1), min(self.height, y2 + 1)):
            for x in range(max(0, x1), min(self.width, x2 + 1)):
                self.buffer[y][x] = char
                self.colors[y][x] = colour
                self.attributes[y][x] = attr

def download_screen(screen, message="DOWNLOADING", duration=None, border=True, description="", 
                             background_color=Screen.COLOUR_BLACK, popup_width=60, popup_height=15, 
                             current_file="", progress=0.0, allow_early_exit=True):
    screen_height, screen_width = screen.dimensions
    
    x_offset = max(0, (screen_width - popup_width) // 2)
    y_offset = max(0, (screen_height - popup_height) // 2)

    buffer = Buffer(popup_width, popup_height)

    start_time = time.time()
    spinner_chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    spinner_index = 0
    last_update = 0

    if allow_early_exit:
        description += "\n\nPress Enter to exit"

    while True:
        current_time = time.time()
        
        if current_time - last_update >= 0.1:
            buffer.fill_rect(0, 0, popup_width - 1, popup_height - 1, colour=background_color)

            if border:
                for x in range(1, popup_width - 1):
                    buffer.print_at('-', x, 0, Screen.COLOUR_BLUE)
                    buffer.print_at('-', x, popup_height - 1, Screen.COLOUR_BLUE)
                for y in range(1, popup_height - 1):
                    buffer.print_at('|', 0, y, Screen.COLOUR_BLUE)
                    buffer.print_at('|', popup_width - 1, y, Screen.COLOUR_BLUE)
                buffer.print_at('+', 0, 0, Screen.COLOUR_BLUE)
                buffer.print_at('+', popup_width - 1, 0, Screen.COLOUR_BLUE)
                buffer.print_at('+', 0, popup_height - 1, Screen.COLOUR_BLUE)
                buffer.print_at('+', popup_width - 1, popup_height - 1, Screen.COLOUR_BLUE)

            # Main message
            x_pos = max(0, (popup_width - len(message)) // 2)
            y_pos = 2
            buffer.print_at(message, x_pos, y_pos, Screen.COLOUR_CYAN, Screen.A_BOLD)

            # Current file display
            if current_file:
                max_file_width = popup_width - 6
                if len(current_file) > max_file_width:
                    current_file = current_file[:max_file_width-3] + "..."
                x_pos = 3
                y_pos = popup_height - 5
                buffer.print_at(current_file, x_pos, y_pos, Screen.COLOUR_WHITE)

            # Progress bar
            progress_width = popup_width - 8
            filled = int(progress_width * progress)
            x_pos = 2
            y_pos = popup_height - 2
            buffer.print_at("[" + "#" * filled + "-" * (progress_width - filled) + "]", x_pos, y_pos, Screen.COLOUR_GREEN)
            progress = min(1.0, (current_time - start_time) / duration if duration else progress)

            # Percentage
            percentage = f"{int(progress * 100)}%"
            x_pos = popup_width - len(percentage) - 4
            y_pos = popup_height - 3
            buffer.print_at(percentage, x_pos, y_pos, Screen.COLOUR_GREEN)

            # Timer
            elapsed_time = int(current_time - start_time)
            timer_text = f"Time: {elapsed_time}s"
            x_pos = 2
            y_pos = 1
            buffer.print_at(timer_text, x_pos, y_pos, Screen.COLOUR_CYAN)

            # Spinner
            buffer.print_at(spinner_chars[spinner_index], popup_width - 2, 1, Screen.COLOUR_MAGENTA)
            spinner_index = (spinner_index + 1) % len(spinner_chars)

            # Description
            if description:
                desc_lines = description.split('\n')
                for i, line in enumerate(desc_lines):
                    x_pos = max(0, (popup_width - len(line)) // 2)
                    y_pos = popup_height - 7 - len(desc_lines) + i
                    buffer.print_at(line, x_pos, y_pos, Screen.COLOUR_WHITE)

            for y in range(popup_height):
                for x in range(popup_width):
                    screen.print_at(buffer.buffer[y][x], x + x_offset, y + y_offset, 
                                    colour=buffer.colors[y][x], attr=buffer.attributes[y][x])

            screen.refresh()
            last_update = current_time

        if allow_early_exit and screen.get_key() == 13:  # Enter key
            break

        if duration is not None and current_time - start_time >= duration:
            break

def run_download_screen(message="DOWNLOADING", duration=None, border=True, description="", 
                        background_color=Screen.COLOUR_BLACK, popup_width=60, popup_height=15, 
                        current_file="", progress=0.0, allow_early_exit=True):
    try:
        if sys.stdin.isatty():
            Screen.wrapper(lambda screen: download_screen(screen, message, duration, border, 
                                                                   description, background_color, popup_width, 
                                                                   popup_height, current_file, progress, 
                                                                   allow_early_exit))
        else:
            raise EnvironmentError("Asciimatics requires a real terminal.")
    except Exception as e:
        print(f"[DOWNLOAD] {message} (Falling back to text mode)")
        print(str(e))