from datetime import datetime

def get_timestamp():
    """Gibt den aktuellen UNIX-Timestamp zurück."""
    return int(datetime.now().timestamp())

def format_date(date: datetime, fmt: str = "%Y-%m-%d %H:%M:%S"):
    """Formatiert ein Datum in ein bestimmtes Format."""
    return date.strftime(fmt)