from Card import Card


class Cards:
    cards = []

    @staticmethod
    def add_card(term, definition):
        Cards.cards.append(Card(term, definition))

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
    def delete_card(term):
        card_found = Cards.find_card(term)
        if card_found:
            Cards.cards.remove(card_found)
            return True
        return False

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
    def log():
        for card in Cards.cards:
            print(card)
