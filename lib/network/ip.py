import os
import requests


def get_ip():
    """Gibt die öffentliche IP-Adresse zurück."""
    return requests.get("https://api64.ipify.org").text

def ping(host: str):
    """Überprüft, ob ein Host erreichbar ist."""
    return os.system(f"ping -c 1 {host} > /dev/null 2>&1") == 0