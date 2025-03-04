def clamp(value, min_value, max_value):
    """Begrenzt einen Wert auf einen bestimmten Bereich."""
    return max(min_value, min(value, max_value))