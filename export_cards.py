from Cards import Cards


def save_cards(f_name):
    try:
        cards_file = open(f_name, "w")

        for card in Cards.cards:
            cards_file.write(f"{card}\n")

        cards_file.close()
    except OSError:
        print("Error: Could not save cards.")
    else:
        print(f"{len(Cards.cards)} cards have been saved.")


def export_cards():
    name = input("File name:\n")
    save_cards(name)

