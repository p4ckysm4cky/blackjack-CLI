from card_deck import Card, Deck

class Player():
    def __init__(self, is_dealer):
        self.deck = Deck()
        self.is_dealer = is_dealer
        self.score = 0
        self.money = 1000

    
    def hit(self, a_card):
        self.deck.add_card(a_card.rank, a_card.suit)


if __name__ == "__main__":
    a_player = Player(is_dealer=False)
    a_deck = Deck()
    a_deck.generate_standard()
    card_drawn = a_deck.draw_card()
    a_player.hit(card_drawn)
    a_player.deck.display_vertical()


    