import json
import os

CONFIG_PATH: str = os.path.join(os.path.dirname(__file__), "config.json")

def load_config() -> dict:
    """Lädt die Konfigurationsdatei."""
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config = json.load(f)
            return config
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError as e:
        return {}

CONFIG: dict = load_config()


def save_config(config: dict) -> None:
    """Speichert die Konfigurationsdatei."""
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4)
    except Exception as e:
        pass  # Handle exceptions if needed

def set_config_path(path: str) -> None:
    """Setzt den Pfad zur Konfigurationsdatei."""
    global CONFIG_PATH
    CONFIG_PATH = path
    
def enableLibLogging() -> None:
    """Aktiviert das Logging für die lib."""
    #l.debug('Logging for lib is enabled.')
    CONFIG["libLogging"] = True
    save_config(CONFIG)

def disableLibLogging() -> None:
    """Deaktiviert das Logging für die lib."""
    #l.debug('Logging for lib is disabled.')
    CONFIG["libLogging"] = False
    save_config(CONFIG)