class Card:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def __str__(self):
        return f'{self.term}:{self.definition}'
