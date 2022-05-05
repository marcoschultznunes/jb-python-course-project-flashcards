from Cards import Cards


def import_cards():
    name = input("File name:\n")
    loaded = 0
    try:
        cards_file = open(name, "r")

        Cards.clear_cards()

        for line in cards_file:
            vals = line.rstrip().split(":")
            Cards.add_card(vals[0], vals[1], vals[2])
            loaded += 1

        cards_file.close()
    except FileNotFoundError:
        print("File not found.")
    else:
        print(f"{loaded} cards have been loaded.")
