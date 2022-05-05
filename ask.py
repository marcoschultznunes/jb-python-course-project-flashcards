from Cards import Cards


def other_term(term, definition):
    for card in Cards.cards:
        if definition == card.definition and term != card.term:
            return card.term
    return False


def ask():
    times = int(input("How many times to ask?\n"))

    if len(Cards.cards) == 0:
        return False

    for i in range(times):
        card = Cards.find_by_id(i % len(Cards.cards))  # repeats when reaches end
        answer = input(f'Print the definition of "{card.term}":\n')
        if answer == card.definition:
            print("Correct!")
        else:
            other = other_term(card.term, answer)
            if other:
                print(f'Wrong. The right answer is "{card.definition}", but your definition is correct for "{other}".')
            else:
                card.add_mistake()
                print(f'Wrong! The right answer is "{card.definition}"')
