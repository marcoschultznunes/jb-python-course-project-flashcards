class Card:
    def __init__(self, term, definition, mistakes=0):
        self.term = term
        self.definition = definition
        self.mistakes = int(mistakes)

    def __str__(self):
        return f'{self.term}:{self.definition}:{self.mistakes}'

    def add_mistake(self):
        self.mistakes += 1
