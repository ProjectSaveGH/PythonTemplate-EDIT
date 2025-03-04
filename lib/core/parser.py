import re
from lib.logger.logger import Logger

l: Logger = Logger(printLog=True)

def parse_custom_time(time_str: str):
    """Parst ein benutzerdefiniertes Zeitformat in Sekunden."""
    l.info(f"Parsing custom time string: {time_str}")
    
    pattern = re.compile(r"(?:(\d+)y)?(?:(\d+)m)?(?:(\d+)w)?(?:(\d+)d)?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?(?:(\d+)s)?$")
    match = pattern.fullmatch(time_str)

    if not match:
        l.error(f"Failed to parse time string: {time_str}")
        return None

    factors = [31536000, 2628000, 604800, 86400, 3600, 60, 1, 0.1]
    
    total_seconds = sum(int(value) * factor for value, factor in zip(match.groups(default="0"), factors))
    l.info(f"Parsed time string '{time_str}' to {total_seconds} seconds")
    return total_seconds
