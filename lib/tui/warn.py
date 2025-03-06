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

def warn_screen(screen, message="WARNING!", duration=3, blink=True, border=True, description="", 
                         background_color=Screen.COLOUR_BLACK, progress=False, countdown=False, 
                         spinner=False, popup_width=40, popup_height=10, allow_early_exit=True):
    screen_height, screen_width = screen.dimensions
    
    x_offset = max(0, (screen_width - popup_width) // 2)
    y_offset = max(0, (screen_height - popup_height) // 2)

    buffer = Buffer(popup_width, popup_height)

    start_time = time.time()
    visible = True
    progress_value = 0
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
                    buffer.print_at('-', x, 0, Screen.COLOUR_YELLOW)
                    buffer.print_at('-', x, popup_height - 1, Screen.COLOUR_YELLOW)
                for y in range(1, popup_height - 1):
                    buffer.print_at('|', 0, y, Screen.COLOUR_YELLOW)
                    buffer.print_at('|', popup_width - 1, y, Screen.COLOUR_YELLOW)
                buffer.print_at('+', 0, 0, Screen.COLOUR_YELLOW)
                buffer.print_at('+', popup_width - 1, 0, Screen.COLOUR_YELLOW)
                buffer.print_at('+', 0, popup_height - 1, Screen.COLOUR_YELLOW)
                buffer.print_at('+', popup_width - 1, popup_height - 1, Screen.COLOUR_YELLOW)

            if not blink or visible:
                x_pos = max(0, (popup_width - len(message)) // 2)
                y_pos = popup_height // 4
                buffer.print_at(message, x_pos, y_pos, Screen.COLOUR_YELLOW, Screen.A_BOLD)
            visible = not visible

            if description:
                desc_lines = description.split('\n')
                for i, line in enumerate(desc_lines):
                    x_pos = max(0, (popup_width - len(line)) // 2)
                    y_pos = popup_height // 2 + i
                    buffer.print_at(line, x_pos, y_pos, Screen.COLOUR_WHITE)

            if progress and duration not in (0, -1, None):
                progress_width = popup_width - 6
                filled = int(progress_width * progress_value)
                buffer.print_at("[" + "#" * filled + "-" * (progress_width - filled) + "]", 2, popup_height - 2, Screen.COLOUR_YELLOW)
                progress_value = min(1.0, (current_time - start_time) / duration)

            if countdown and duration not in (0, -1, None):
                remaining = max(0, int(duration - (current_time - start_time)))
                countdown_text = f"Time: {remaining}s"
                buffer.print_at(countdown_text, popup_width - len(countdown_text) - 1, 1, Screen.COLOUR_YELLOW)

            if spinner:
                buffer.print_at(spinner_chars[spinner_index], 1, 1, Screen.COLOUR_CYAN)
                spinner_index = (spinner_index + 1) % len(spinner_chars)

            for y in range(popup_height):
                for x in range(popup_width):
                    screen.print_at(buffer.buffer[y][x], x + x_offset, y + y_offset, 
                                    colour=buffer.colors[y][x], attr=buffer.attributes[y][x])

            screen.refresh()
            last_update = current_time

        if allow_early_exit and screen.get_key() == 13:
            break

        if duration not in (0, -1, None) and current_time - start_time >= duration:
            break

def run_warn_screen(message="WARNING!", duration=3, blink=True, border=True, description="", 
                    background_color=Screen.COLOUR_BLACK, progress=False, countdown=False, 
                    spinner=False, popup_width=40, popup_height=10, allow_early_exit=True):
    try:
        if sys.stdin.isatty():  # Check if the script is running in a real terminal
            #Hide the Cursor
            sys.stdout.write("\033[?25l")
            sys.stdout.flush()
            Screen.wrapper(lambda screen: warn_screen(screen, message, duration, blink, border, 
                                                                description, background_color, progress, 
                                                                countdown, spinner, popup_width, popup_height,
                                                                allow_early_exit), catch_interrupt=True)
        else:
            raise EnvironmentError("Asciimatics requires a real terminal.")
    except Exception as e:
        print(f"[WARN] {message} (Falling back to text mode)")
        print(str(e))
    finally:
        # Ensure the cursor is shown again
        sys.stdout.write("\033[?25h")
        sys.stdout.flush()