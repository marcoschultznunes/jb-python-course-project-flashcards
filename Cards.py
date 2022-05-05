from Card import Card


class Cards:
    cards = []

    @staticmethod
    def add_card(term, definition, mistakes=0):
        Cards.cards.append(Card(term, definition, mistakes))

    @staticmethod
    def find_card(term):
        for card in Cards.cards:
            if card.term == term:
                return card
        return False

    @staticmethod
    def find_by_id(id):
        if id > len(Cards.cards) - 1:
            return False
        return Cards.cards[id]

    @staticmethod
    def find_hardest():
        if len(Cards.cards) == 0:
            return None
        most_mistakes = max(list(map(lambda c: c.mistakes, Cards.cards)))
        hardest = list(filter(lambda c: c.mistakes == most_mistakes, Cards.cards))
        return hardest if most_mistakes > 0 else None

    @staticmethod
    def delete_card(term):
        card_found = Cards.find_card(term)
        if card_found:
            Cards.cards.remove(card_found)
            return True
        return False

    @staticmethod
    def clear_cards():
        Cards.cards = []

    @staticmethod
    def check_if_term_exists(term):
        for card in Cards.cards:
            if term == card.term:
                return True
        return False

    @staticmethod
    def check_if_def_exists(definition):
        for card in Cards.cards:
            if definition == card.definition:
                return True
        return False

    @staticmethod
    def reset_stats():
        for c in Cards.cards:
            c.mistakes = 0

    @staticmethod
    def log():
        print(*Cards.cards, sep="\n")
