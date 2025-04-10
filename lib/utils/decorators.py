import functools
from tkinter import messagebox
from lib.logger.logger import Logger
from lib.config.loader import CONFIG

l: Logger = Logger(printLog=CONFIG["libLogging"])

def deactive(reason="Diese Funktion ist deaktiviert."):
    """Ein Decorator, der eine Funktion deaktiviert."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            l.info(f"Function '{func.__name__}' is deactivated: {reason}")
            messagebox.showerror(f"Funktion '{func.__name__}' ist deaktiviert: {reason}")
        return wrapper
    return decorator