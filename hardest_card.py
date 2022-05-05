from Cards import Cards


def hardest_card():
    cards = Cards.find_hardest()
    if not cards:
        print("There are no cards with errors.")
    elif len(cards) == 1:
        print(f'The hardest card is "{cards[0].term}". You have {cards[0].mistakes} errors answering it.')
    else:
        terms = ", ".join(list(map(lambda c: '"' + c.term + '"', cards)))
        print(f'The hardest cards are {terms}. You have {cards[0].mistakes} errors answering them.')
