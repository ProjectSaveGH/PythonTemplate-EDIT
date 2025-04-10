from .logger import Logger
from ..config.loader import CONFIG
import shutil
import os

l: Logger = Logger(CONFIG["libLogging"])

def get_log_file_path() -> str:
    """
    Get the log file path based on the log type.
    
    Returns:
        str: The path to the log file.
    """
    # Get the base directory for logs from the configuration
    l.info("Getting log file path")
    return CONFIG["paths"]["log_file"]

def clear_log_file() -> None:
    """
    Clear the log file for the specified log type.
    """
    # Get the path to the log file
    log_file_path = get_log_file_path()
    
    # Clear the contents of the log file
    l.info(f"Clearing log file at {log_file_path}")
    with open(log_file_path, 'w') as file:
        file.write('')  # Write an empty string to clear the file

    # Log the action
    l.info(f"Cleared log file at {log_file_path}")

def backup_log():
    """
    Backup the log file by renaming it with a timestamp.
    """    
    count = 0
    while True:
        try:
            if os.path.exists(get_log_file_path() + f".bak{count if count > 0 else ''}"):
                # If the backup file already exists, raise FileExistsError
                raise FileExistsError
            
            shutil.copy(get_log_file_path(), get_log_file_path() + f".bak{count if count > 0 else ''}")
            l.info(f"Backed up log file to {get_log_file_path() + f'.bak{count if count > 0 else ''}'}")
            break
        except FileExistsError:
            # If the backup file already exists, increment the count and try again
            l.warn(f"Backup file already exists, incrementing count to {count + 1}")
            count += 1
    
    l.info(f"Backup log file at {get_log_file_path() + f'.bak{count if count > 0 else ''}'}")
    os.remove(get_log_file_path())