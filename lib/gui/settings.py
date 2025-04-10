from pathlib import Path
import customtkinter as ctk
import json
from tkinter import messagebox
from lib.logger.logger import Logger
from lib.config.loader import CONFIG

l: Logger = Logger(printLog=CONFIG["libLogging"])


def get_possible_values(config, x):
    try:
        return config.get("selection", {}).get(x, [])
    except KeyError:
        l.warn(f"KeyError: {x} not found in config selection.")
        return []


def is_boolean(key):
    return key.startswith("%bool%")


def load_settings(config_file: str | Path):
    try:
        with open(config_file, "r") as configfile:
            config = json.load(configfile)
            settings = config.get("settings", {})
            l.info(f"Settings loaded from {config_file}")
            return config, settings
    except FileNotFoundError:
        l.error(f"Config file not found: {config_file}")
        return None, {}
    except json.JSONDecodeError as e:
        l.error(f"Error decoding JSON from {config_file}: {e}")
        return None, {}


def save_settings(config, settings_widgets):
    try:
        for key, widget in settings_widgets.items():
            if isinstance(widget, ctk.CTkSwitch):
                config["settings"][key] = "true" if widget.get() else "false"
            elif isinstance(widget, ctk.CTkOptionMenu):
                config["settings"][key] = widget.get()
            elif isinstance(widget, ctk.CTkEntry):
                config["settings"][key] = widget.get()

        with open("settings.json", "w") as configfile:
            json.dump(config, configfile, indent=4)

        l.info("Settings saved successfully.")
        messagebox.showinfo("Settings", "Settings saved successfully!")
    except Exception as e:
        l.error(f"Error saving settings: {e}")
        messagebox.showerror("Error", "Failed to save settings.")


def open_settings(config_file: str | Path, app_name: str, geometry: str):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")

    root = ctk.CTk()
    root.title(f"{app_name} Settings")
    root.geometry(geometry)

    config, settings = load_settings(config_file)
    if config is None:
        l.error("Config file not found!")
        return

    settings_widgets = {}
    row = 0
    width = int(geometry.split("x")[0])

    for key, value in settings.items():
        label = ctk.CTkLabel(root, text=f"{key.removeprefix('%bool%').capitalize()}")
        label.grid(row=row, column=0, sticky="w", padx=10, pady=5)

        if is_boolean(key):
            current_value = value == "true"
            switch = ctk.CTkSwitch(
                root,
                text="",
                variable=ctk.BooleanVar(value=current_value),
            )
            switch.grid(row=row, column=1, padx=10, pady=5)
            settings_widgets[key] = switch
        else:
            possible_values = get_possible_values(config, key)
            if possible_values:
                selected_value = value
                dropdown = ctk.CTkOptionMenu(
                    root,
                    values=possible_values,
                    variable=ctk.StringVar(value=selected_value),
                    width=int(width*0.9)
                )
                dropdown.grid(row=row, column=1, padx=10, pady=5)
                settings_widgets[key] = dropdown
            else:
                entry = ctk.CTkEntry(root, placeholder_text=f"Enter {key}", width=int(width*0.9))
                entry.insert(0, value)
                entry.grid(row=row, column=1, padx=10, pady=5)
                settings_widgets[key] = entry

        row += 1

    save_button = ctk.CTkButton(
        root,
        text="Save Settings",
        command=lambda: save_settings(config, settings_widgets),
    )
    save_button.grid(row=row, columnspan=2, pady=10)

    l.info("Settings window opened.")
    root.mainloop()