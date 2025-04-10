from pathlib import Path
from customtkinter import CTk, CTkEntry, CTkLabel, CTkButton, CTkImage
from PIL import Image
import customtkinter
import sqlite3
from lib.logger.logger import Logger
from lib.config.loader import CONFIG

l: Logger = Logger(printLog=CONFIG["libLogging"])

APPLICATION_NAME: str = ""
APPLICATION_GEOMETRIE: str = ""

WINDOW_HEIGHT: int = 0
WINDOW_WIDTH: int = 0

BG_IMAGE: str | None = None

OUTPUT: bool | tuple[bool, str] = False

l.debug("Opening Login Window with \'customtkinter - CTk\'")

def settings():
    global root
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = CTk()

    root.title(f"{APPLICATION_NAME} Login")
    root.geometry(APPLICATION_GEOMETRIE)
    root.resizable(False, False)


def modules(bg_img: str | None, database: str | Path):
    try:
        if bg_img:
            bg_image = CTkImage(Image.open(bg_img),
                                size=(WINDOW_WIDTH, WINDOW_HEIGHT))
            bg_image_label = CTkLabel(root, image=bg_image, text="")
            bg_image_label.place(x=0, y=0)

    except FileNotFoundError:
        raise FileNotFoundError(f"Background Image not found: {bg_img}")
    except Exception as e:
        raise e

    title_label = CTkLabel(root, text=f"{APPLICATION_NAME} Login", font=("Monospace", 20))
    info_label = CTkLabel(root, text=f"Please Login to {APPLICATION_NAME}", font=("Monospace", 10))
    title_label.pack(padx=10)
    info_label.pack(padx=10)

    global username_entry
    username_entry = CTkEntry(root, width=( int(WINDOW_WIDTH*0.8) ), placeholder_text="Username")
    username_entry.pack(padx=10, pady=10)

    password_entry = CTkEntry(root, show="*", width=( int(WINDOW_WIDTH*0.8) ), placeholder_text="Password")
    password_entry.pack(padx=10, pady=10)

    global status_label
    status_label = CTkLabel(root, text="", font=("Monospace", 10))
    status_label.pack(padx=10, pady=10)

    login_button = CTkButton(root, text="Login", width=( int(WINDOW_WIDTH*0.6) ), command=lambda: login(username_entry.get(), password_entry.get(), database))
    login_button.pack(padx=10, pady=25)


def login(username: str, password: str, database: str | Path) -> None:
    global OUTPUT
    l.info(f"Trying to login with username: {username} and password: {len(password)*'*'}")

    while True:
        if not username:
            l.warn("Username is empty.")
            status_label.configure(text="Username is empty.")
            return
        if not password:
            l.warn("Password is empty.")
            status_label.configure(text="Password is empty.")
            return
        break

    conn = sqlite3.connect(database)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE LOWER(username) = LOWER(?)", (username,))
    user = cursor.fetchone()

    conn.close()

    if user:
        l.info(f"User {username} found in the database.")
        if user[1] == password:
            l.info("Password is correct.")
            status_label.configure(text="Login successful. Redicting...")
            OUTPUT = (True, username)
            root.destroy()
        else:
            l.warn("Password is incorrect.")
            status_label.configure(text="Username or Password is incorrect.")
            OUTPUT = False
    else:
        l.warn(f"User {username} not found in the database.")
        status_label.configure(text="Username or Password is incorrect.")
        OUTPUT = False


def open_login(app_name: str, app_geo: str, database: str | Path, bg_image: str | None = None):
    global APPLICATION_NAME, APPLICATION_GEOMETRIE, WINDOW_HEIGHT, WINDOW_WIDTH
    APPLICATION_NAME = app_name
    APPLICATION_GEOMETRIE = app_geo
    WINDOW_WIDTH, WINDOW_HEIGHT = int(app_geo.split("x")[0]), int(app_geo.split("x")[1])

    BG_IMAGE = bg_image if bg_image else None


    settings()
    modules(BG_IMAGE, database)
    
    root.mainloop()
    return OUTPUT
