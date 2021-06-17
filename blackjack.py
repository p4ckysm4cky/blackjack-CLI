from card_deck import Card, Deck
from time import sleep


class Player():
    def __init__(self, is_dealer):
        self.deck = Deck()
        self.is_dealer = is_dealer
        self.score = 0
        if not is_dealer:
            self.money = 5000
            self.bet = 0
        self.ace_count = 0

    
    def hit(self, a_card, hidden=False):
        self.deck.add_card(a_card.rank, a_card.suit, hidden)

    def get_deck(self):
        return self.deck


    def get_money(self):
        return self.money


    def place_bet(self):
        while True:
            bet = int(input("Please enter how much you wish to bet: "))
            if bet <= self.money:
                self.bet += bet
                self.money -= bet
                return bet 
            else:
                print("The bet you entered is more than the amount you have")
                sleep(0.5)

    
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


    def reset_hand(self):
        return self.deck.reset_deck()

    
    def reset_score(self):
        self.score = 0




class Blackjack():
    def __init__(self, rounds):
        self.rounds = rounds
        self.player = Player(is_dealer=False)
        self.dealer = Player(is_dealer=True)

    
    def start(self):
        print("""
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/                 
                      """)
    
    def bet_input(self):
        while True:
            try: 
                return self.player.place_bet()
            except:
                print("Invalid input, try again")
                sleep(0.5)


    def initial_deal(self, standard_deck):
        self.player.hit(standard_deck.draw_card())
        self.dealer.hit(standard_deck.draw_card())
        self.player.hit(standard_deck.draw_card())
        self.dealer.hit(standard_deck.draw_card(), hidden=True)



    
    def main(self):
        self.start()
        blackjack_deck = Deck()
        blackjack_deck.generate_standard()
        blackjack_deck.shuffle()

        for i in range(1, self.rounds + 1):
            print("="*30)
            print(f"Round {i}")
            print(f"Current balance: {self.player.get_money()}")
            bet_amount = self.bet_input()
            self.initial_deal(blackjack_deck)
            self.dealer.get_deck().display_horizontal()
            print("-"*30)
            self.player.get_deck().display_horizontal()

            return



    


    


if __name__ == "__main__":

    a = Blackjack(5)
    a.main()



    