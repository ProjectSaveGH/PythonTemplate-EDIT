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
