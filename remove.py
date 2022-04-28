from Cards import Cards


def remove():
    term = input("Which card?\n")
    if Cards.delete_card(term):
        print("The card has been removed.")
    else:
        print(f'Can\'t remove "{term}": there is no such card.')
