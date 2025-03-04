import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def extract_phone_numbers(text: str) -> list:
    pattern = r'\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}'
    return re.findall(pattern, text)

def remove_html_tags(text: str) -> str:
    return re.sub(r'<.*?>', '', text)

def extract_urls(text: str) -> list:
    pattern = r'https?://(?:www\.)?\S+'
    return re.findall(pattern, text)

def find_words_of_length(text: str, length: int) -> list:
    pattern = rf'\b\w{{{length}}}\b'
    return re.findall(pattern, text)

def is_strong_password(password: str) -> bool:
    pattern = r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    return bool(re.match(pattern, password))

def camel_to_snake(name: str) -> str:
    name = re.sub(r'([a-z])([A-Z])', r'\1_\2', name)
    return name.lower()

def snake_to_camel(name: str) -> str:
    return ''.join(word.capitalize() for word in name.split('_'))

def remove_duplicate_words(text: str) -> str:
    return re.sub(r'\b(\w+)( \1\b)+', r'\1', text)

def extract_dates(text: str) -> list:
    pattern = r'\b(?:\d{2}\.\d{2}\.\d{4}|\d{4}-\d{2}-\d{2})\b'
    return re.findall(pattern, text)

def find_capitalized_words(text: str) -> list:
    return re.findall(r'\b[A-Z][a-z]*\b', text)

def remove_special_chars(text: str) -> str:
    return re.sub(r'[^A-Za-z0-9 ]+', '', text)

def is_valid_ipv4(ip: str) -> bool:
    pattern = r'^((25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|1?[0-9][0-9]?)$'
    return bool(re.match(pattern, ip))

def extract_hashtags(text: str) -> list:
    return re.findall(r'#\w+', text)

def is_valid_uuid(uuid: str) -> bool:
    pattern = r'^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$'
    return bool(re.match(pattern, uuid))

def remove_extra_spaces(text: str) -> str:
    return re.sub(r'\s+', ' ', text).strip()

def replace_digits_with_words(text: str) -> str:
    num_map = {'0': 'zero', '1': 'one', '2': 'two', '3': 'three', '4': 'four',
               '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
    return re.sub(r'\d', lambda x: num_map[x.group()], text)

def has_duplicate_word(text: str) -> bool:
    return bool(re.search(r'\b(\w+)\b.*\b\1\b', text))

def find_abbreviations(text: str) -> list:
    return re.findall(r'\b[A-Z]{2,}(?:\.[A-Z]{2,})*\b', text)

def remove_numbers(text: str) -> str:
    return re.sub(r'\d+', '', text)

def words_starting_with(text: str, letter: str) -> list:
    pattern = rf'\b{letter}\w*\b'
    return re.findall(pattern, text, re.IGNORECASE)
