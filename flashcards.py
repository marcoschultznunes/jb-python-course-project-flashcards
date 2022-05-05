from add import add
from remove import remove
from ask import ask
from import_cards import import_cards
from export_cards import export_cards
from hardest_card import hardest_card
from reset_stats import reset_stats
from log import save_log, LoggerIn, LoggerOut
import sys


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
    sys.stdout = LoggerOut()
    sys.stdin = LoggerIn()

    while main_menu() != "exit":
        pass


main()
print("bye bye")
