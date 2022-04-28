from add import add
from remove import remove
from ask import ask
from import_cards import import_cards
from export_cards import export_cards


def main_menu():
    opt = input("Input the action (add, remove, import, export, ask, exit):\n")
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


def main():
    while main_menu() != "exit":
        pass


main()
print("bye bye")
