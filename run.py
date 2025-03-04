from rich.traceback import install
import time
from lib.startup.functions import pre_tasks, post_tasks
from lib.logger.logger import Logger
from lib.cli.arguments import parse_args, add_arg, argparse

l: Logger = Logger(printLog=True)
install()

def run_main(file_name="main.py", func_name="main"):
    """
    Importiert die angegebene Datei und führt die angegebene Funktion aus.
    Es wird vorausgesetzt, dass die Datei stets die angegebene Funktion enthält.
    """
    l.info(f"Importiere und starte {func_name}() aus {file_name}...")
    try:
        module_name = file_name.replace(".py", "")
        main_module = __import__(module_name)
        l.debug(f"Import von {file_name} erfolgreich.")
    except ImportError as e:
        l.critical(f"Fehler beim Importieren von {file_name}: {e}")
        return

    if hasattr(main_module, func_name):
        getattr(main_module, func_name)()
    else:
        l.error(f"{file_name} enthält keine {func_name}()-Funktion!")

def main():
    parser = argparse.ArgumentParser()

    add_arg(parser=parser, name="--file", help_text="Name der Datei, die ausgeführt werden soll.", default="main.py")
    add_arg(parser=parser, name="--func", help_text="Name der Funktion, die ausgeführt werden soll.", default="main")

    args = parse_args(parser=parser)
    file_name = args.file #type: ignore
    func_name = args.func #type: ignore
    
    pre_tasks()
    start_time = time.time()
    run_main(file_name, func_name)
    execution_time = time.time() - start_time
    post_tasks(execution_time)

if __name__ == "__main__":
    main()