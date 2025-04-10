import argparse
from argparse import ArgumentParser
from lib.logger.logger import Logger
from lib.config.loader import CONFIG

l: Logger = Logger(printLog=CONFIG["libLogging"])

def add_arg(parser: ArgumentParser, name: str, help_text: str, default: str | None = None, action: str | None = None, required: bool = False) -> None:
    """Fügt ein Argument mit optionalen Werten hinzu."""
    l.info(f"Adding argument: {name}, help: {help_text}, default: {default}, action: {action}, required: {required}")
    if required and action:
        parser.add_argument(name, help=help_text, default=default, action=action, required=required)
    elif required:
        parser.add_argument(name, help=help_text, required=required)
    elif action:
        parser.add_argument(name, help=help_text, default=default, action=action)
    else:
        parser.add_argument(name, help=help_text, default=default)

def parse_args(parser: ArgumentParser) -> dict[str, str]:
    l.info("Parsing arguments")
    parser.add_argument("--debug", action="store_true", help="Debug-Modus aktivieren")
    args = parser.parse_args()
    l.info(f"Arguments parsed: {args}")
    return args #type: ignore
