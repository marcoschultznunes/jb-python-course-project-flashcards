from Cards import Cards


def get_new_term_if_dupe(term):
    while Cards.check_if_term_exists(term):
        term = input(f'The card "{term}" already exists. Try again:\n')
    return term


def get_new_def_if_dupe(definition):
    while Cards.check_if_def_exists(definition):
        definition = input(f'The definition "{definition}" already exists. Try again:\n')
    return definition


def add():
    term = input("The card:\n")
    term = get_new_term_if_dupe(term)
    definition = input("The definition of the card:\n")
    definition = get_new_def_if_dupe(definition)
    Cards.add_card(term, definition)
    print(f'The pair ("{term}":"{definition}") has been added.')
