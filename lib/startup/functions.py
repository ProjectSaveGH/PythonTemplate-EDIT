#!/usr/bin/env python3
import os
import sys
import shutil
from rich.traceback import install
from lib.logger.logger import Logger

l: Logger = Logger(printLog=True)

def clean_pycaches(root_dir, show: bool = False):
    """Durchsucht rekursiv das angegebene Verzeichnis und entfernt alle __pycache__-Ordner."""
    l.info(f"Bereinige __pycache__-Ordner im Verzeichnis: {root_dir}")
    for root, dirs, _ in os.walk(root_dir):
        if "__pycache__" in dirs:
            pycache_path = os.path.join(root, "__pycache__")
            try:
                shutil.rmtree(pycache_path)
                l.info(f"Gelöscht: {pycache_path}")
                # print(f"Gelöscht: {pycache_path}") if show else None
            except Exception as e:
                l.error(f"Fehler beim Löschen von {pycache_path}: {e}")

def check_environment():
    """Überprüft die Systemumgebung, z. B. die Python-Version."""
    l.info("Überprüfe die Systemumgebung...")
    l.debug(f"Python-Version im Detail: {sys.version_info}")
    if sys.version_info < (3, 6):
        l.warn("Python-Version ist veraltet. Empfohlen wird Python 3.6 oder höher.")
    else:
        l.info(f"Aktuelle Python-Version: {sys.version}")

def backup_config():
    """Erstellt ein Backup der Konfigurationsdatei, falls vorhanden."""
    config_file = "config.yaml"
    l.info(f"Erstelle Backup der Konfiguration ({config_file})...")
    if os.path.isfile(config_file):
        backup_file = config_file + ".bak"
        try:
            shutil.copyfile(config_file, backup_file)
            l.info(f"Backup erfolgreich erstellt: {backup_file}")
        except Exception as e:
            l.error(f"Fehler beim Erstellen des Backups: {e}")
    else:
        l.info(f"Keine Konfigurationsdatei '{config_file}' gefunden. Überspringe Backup.")

def pre_tasks():
    """Führt alle notwendigen Vorarbeiten durch."""
    l.info("Starte Vorbereitungsarbeiten...")
    install()
    check_environment()
    backup_config()
    l.info("Alle Vorbereitungsarbeiten wurden erfolgreich abgeschlossen.")

def log_performance(execution_time):
    """Protokolliert die Ausführungsdauer der main()-Funktion."""
    l.info(f"Die Ausführung von main() dauerte {execution_time:.2f} Sekunden.")

def cleanup_resources():
    """Bereinigt nach der Ausführung temporäre Ressourcen."""
    temp_dir = "temp"
    l.info(f"Starte Aufräumarbeiten im temporären Verzeichnis: {temp_dir}")
    if os.path.isdir(temp_dir):
        try:
            shutil.rmtree(temp_dir)
            l.info(f"Temporäres Verzeichnis '{temp_dir}' wurde gelöscht.")
        except Exception as e:
            l.error(f"Fehler beim Löschen des temporären Verzeichnisses '{temp_dir}': {e}")
    else:
        l.info(f"Kein temporäres Verzeichnis '{temp_dir}' gefunden.")

def post_tasks(execution_time):
    """Führt alle notwendigen Nacharbeiten durch."""
    l.info("Starte Nachbereitungsarbeiten...")
    log_performance(execution_time)
    clean_pycaches(".")
    cleanup_resources()
    l.info("Alle Nachbereitungsarbeiten wurden erfolgreich abgeschlossen.")