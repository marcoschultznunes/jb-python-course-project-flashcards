from Cards import Cards


def export_cards():
    name = input("File name:\n")

    try:
        cards_file = open(name, "w")

        for card in Cards.cards:
            cards_file.write(f"{card}\n")

        cards_file.close()
    except OSError:
        print("Error: Could not save cards.")
    else:
        print(f"{len(Cards.cards)} cards have been saved.")
