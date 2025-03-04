import random
import string

def random_string(length=10):
    """Generiert einen zufälligen String der angegebenen Länge."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))