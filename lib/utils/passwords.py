import hashlib
import secrets
import string
try:
    import msvcrt
except ImportError:
    msvcrt = None

def input_pwsd(prompt: str, mask: str = "*") -> str:
    """Reads a password from user input with masked characters."""

    print(prompt, end="", flush=True)
    password = []
    
    while True:
        try:
            char = msvcrt.getch()
        except TypeError:
            print("MSVCRT module not available.")
            break
        if char in {b"\r", b"\n"}:
            print()
            break
        elif char == b"\x08":  # Backspace
            if password:
                password.pop()
                print("\b \b", end="", flush=True)
        elif char.decode("utf-8").isprintable():
            password.append(char.decode("utf-8"))
            print(mask, end="", flush=True)
    
    return "".join(password)

def hash_password(password: str, salt: str = "") -> str:
    """Hashes a password using SHA-256 with an optional salt."""
    return hashlib.sha256((salt + password).encode()).hexdigest()

def generate_password(length: int = 12, use_digits: bool = True, use_special: bool = True) -> str:
    """Generates a random password with given length and complexity options."""
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    return "".join(secrets.choice(characters) for _ in range(length))

def strong_password_check(password: str, min_length: int = 8) -> bool:
    """Checks if a password meets strength requirements."""
    if len(password) < min_length:
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False
    return True
