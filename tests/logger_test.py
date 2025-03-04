import os
from lib.logger.logger import Logger

# Initialize logger
logger = Logger(printLog=True)

def main():
    logger.debug("Debug message")
    logger.info("Hello, World!")
    logger.warn("Warning message")
    logger.error("Error message")
    logger.critical("Critical message")
    logger.critical("Critical exit message", exit=True, exit_code=100)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    main()