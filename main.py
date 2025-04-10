from lib.config.loader import enableLibLogging as eLL
from lib.logger.loggerFileUtils import get_log_file_path, clear_log_file, backup_log
from lib.logger.logger import Logger

l: Logger = Logger(True)

eLL()
l.info(get_log_file_path())
l.info("Backing up log file...")
backup_log()
l.info("Clearing log file...")
clear_log_file()
