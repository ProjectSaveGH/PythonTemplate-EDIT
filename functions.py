from lib.startup.functions import clean_pycaches
from lib.cli.arguments import parse_args, add_arg
from argparse import ArgumentParser

standard_parser = ArgumentParser()
add_arg(standard_parser, "--clean_pycache", "Cleans every PyCache in this folder", action="store_true", required=False)

args = parse_args(standard_parser)

if args.clean_pycache: #type: ignore
    clean_pycaches(".", show=True)
else:
    print("No arguments given.")