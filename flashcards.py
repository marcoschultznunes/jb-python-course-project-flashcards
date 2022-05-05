from add import add
from remove import remove
from ask import ask
from import_cards import import_cards, load_cards
from export_cards import export_cards, save_cards
from hardest_card import hardest_card
from reset_stats import reset_stats
from log import save_log, LoggerIn, LoggerOut
import sys
import argparse


def main_menu():
    opt = input("Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n")
    if opt == "add":
        add()
    elif opt == "remove":
        remove()
    elif opt == "import":
        import_cards()
    elif opt == "export":
        export_cards()
    elif opt == "ask":
        ask()
    elif opt == "exit":
        return "exit"
    elif opt == "log":
        save_log()
    elif opt == "hardest card":
        hardest_card()
    elif opt == "reset stats":
        reset_stats()


def main():
    # Logging inputs and outputs
    sys.stdout = LoggerOut()
    sys.stdin = LoggerIn()

    # arguments => import and export
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument("--import_from", type=str)
    arg_parser.add_argument("--export_to", type=str)
    args = arg_parser.parse_args()

    if args.import_from:
        load_cards(args.import_from)

    while main_menu(args) != "exit":
        pass

    if args.export_to:
        save_cards(args.export_to)  # export when exit && arg


main()
print("bye bye")
