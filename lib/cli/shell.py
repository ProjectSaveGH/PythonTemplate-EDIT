import os
import subprocess

def clear_console():
    """Löscht die Konsole."""
    os.system('cls' if os.name == 'nt' else 'clear')

def run_command(cmd):
    """Führt einen Shell-Befehl aus und gibt die Ausgabe zurück."""
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return result.stdout.strip()