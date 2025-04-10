import os
import shutil
from lib.logger.logger import Logger
from lib.config.loader import CONFIG

l: Logger = Logger(printLog=CONFIG["libLogging"])

def create_folder(path):
    """Erstellt einen Ordner, falls er nicht existiert."""
    l.info(f"Creating folder: {path}")
    os.makedirs(path, exist_ok=True)
    l.info(f"Folder created: {path}")

def delete_folder(path):
    """Löscht einen Ordner und dessen Inhalt."""
    l.info(f"Deleting folder: {path}")
    if os.path.exists(path):
        shutil.rmtree(path)
        l.info(f"Folder deleted: {path}")
    else:
        l.warn(f"Folder not found: {path}")

def read_file(file_path):
    """Liest den Inhalt einer Datei."""
    l.info(f"Reading file: {file_path}")
    try:
        with open(file_path, 'r', encoding="utf-8") as f:
            content = f.read()
            l.info(f"File read successfully: {file_path}")
            return content
    except FileNotFoundError:
        l.error(f"File not found: {file_path}")
        return None

def write_file(file_path, content):
    """Schreibt Inhalt in eine Datei."""
    l.info(f"Writing to file: {file_path}")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write(content)
    l.info(f"File written successfully: {file_path}")

def append_file(file_path, content):
    """Schreibt Inhalt in eine Datei."""
    l.info(f"Appending to file: {file_path}")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'a', encoding="utf-8") as f:
        f.write(content)
    l.info(f"File appended successfully: {file_path}")

def delete_file(file_path):
    """Löscht eine Datei."""
    l.info(f"Deleting file: {file_path}")
    if os.path.exists(file_path):
        os.remove(file_path)
        l.info(f"File deleted: {file_path}")
    else:
        l.warn(f"File not found: {file_path}")
