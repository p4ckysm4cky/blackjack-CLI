from card_deck import Card, Deck


class Player():
    def __init__(self, is_dealer):
        self.deck = Deck()
        self.is_dealer = is_dealer
        self.score = 0
        self.money = 1000
        self.ace_count = 0

    
    def hit(self, a_card):
        self.deck.add_card(a_card.rank, a_card.suit)


    def get_money(self):
        return self.money

    
    def add_money(self, amount):
        self.money += amount


    def minus_money(self, amount):
        self.money -= amount

    
    def get_score(self):
        for card in self.deck.get_cards():
            if card.get_rank().isdigit():
                self.score += int(card.get_rank())
            elif card.get_rank() in ["J", "Q", "K"]:
                self.score += 10
            else:
                self.score += 11
                self.ace_count += 1

        while self.score > 21 and self.ace_count > 0:
            self.score -= 10
            self.ace_count -= 1

        return self.score



    

    
    def reset_score(self):
        self.score = 0

    


    


if __name__ == "__main__":
    a_player = Player(is_dealer=False)
    a_player.hit(Card("A", "S"))
    a_player.hit(Card("K", "D"))
    a_player.hit(Card("J", "S"))
    print(a_player.get_score())


    