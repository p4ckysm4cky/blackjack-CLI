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

    def reset_bet(self):
        """
        This is used to reset the bet amount of each round
        """
        self.bet = 0

    def get_deck(self):
        return self.deck


    def get_money(self):
        return self.money


    def place_bet(self):
        """
        Prompts the user to input bet amount, which decreases self.money and returns bet integer
        """
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
        """
        Calculates score of a player's hand (deck) while taking account aces
        """
        # reset the score for every count
        self.score = 0
        # reset ace count for every count
        self.ace_count = 0
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
        print("Dealing...")
        sleep(0.5)
        self.player.hit(standard_deck.draw_card())
        self.dealer.hit(standard_deck.draw_card())
        self.player.hit(standard_deck.draw_card())
        self.dealer.hit(standard_deck.draw_card(), hidden=True)


    def natural_blackjack(self, bet_amount):
        self.dealer.get_deck().hide_card(1, False)
        if self.dealer.get_score() == 21:
            self.display_current()
            print("Push")
            self.player.add_money(bet_amount)
            print(f"You received {bet_amount} back")
        else:
            self.display_current()
            print("Congrats you got a natural blackjack!")
            pay_amount = round(bet_amount * 2.5)
            self.player.add_money(pay_amount)
            print(f"You received {pay_amount} (1.5 times normal!)")

            



    def card_split(self):
        pass


    def card_double(self):
        pass


    def display_current(self):
        """
        Displays current cards of dealer and player
        """
        self.dealer.get_deck().display_horizontal()
        print("-"*30)
        self.player.get_deck().display_horizontal()
        print(f"Player score: {self.player.get_score()}")
        if self.player.get_score() > 21:
            print("Bust!")

    
    def dealer_draw(self, blackjack_deck):
        """
        Makes the dealer draw cards from blackjack_deck until their score is over 17
        """
        while self.dealer.get_score() < 17:
            self.dealer.hit(blackjack_deck.draw_card())


    def available_options(self, bet_amount, is_first_time=False):
        """
        Basically it displays the available options that the user are allowed to choose from
        """
        options = ["hit", "stand"]
        if self.player.get_score() == 21 and is_first_time:
            return "natural_blackjack"
        else:
            if is_first_time and self.player.get_money() >= bet_amount:
                # you can only double during your first move
                options.append("double")

            if self.player.get_deck().get_cards()[0].get_rank() == self.player.get_deck().get_cards()[1].get_rank() and is_first_time and self.player.get_money() >= bet_amount:
                # split is available if same rank, and first move
                options.append("split")
            
            # Probably in future iterations add insurance and etc to the options
            
        print("Moves:", end =" ")
        [print(f"[{choice}]", end = " ") for choice in options]
        print()

        while True:
            try:
                user_input = input("Input your choice: ").lower()
                if user_input in options:
                    return user_input
                else:
                    print("Invalid input")
                    sleep(0.5)
            except:
                print("Invalid input")
                sleep(0.5)



    # If I have time I might clean this up and break it into separate functions / methods
    def main(self):
        self.start()
        blackjack_deck = Deck()
        original_amount = self.player.get_money
        blackjack_deck.generate_standard()
        blackjack_deck.shuffle()


        for i in range(1, self.rounds + 1):            
            is_player_not_bust = True # used to check if the dealer needs to draw cards
            not_natural_blackjack = True
            
            print("="*30)
            print(f"Card count: {blackjack_deck.deck_length()}")
            print(f"Round {i}")
            print(f"Current balance: ${self.player.get_money()}")
            bet_amount = self.bet_input()
            self.initial_deal(blackjack_deck)
            self.display_current()
            user_input = self.available_options(bet_amount, is_first_time=True)
            while True:
                if user_input == "hit":
                    self.player.hit(blackjack_deck.draw_card())
                elif user_input == "stand":
                    break
                elif user_input == "split":
                    self.card_split()
                elif user_input == "double":
                    self.card_double()
                    break
                elif user_input == "natural_blackjack":
                    not_natural_blackjack = False
                    self.natural_blackjack(bet_amount)
                    break

                else:
                    break

                # After every selection it checks if the player has bust or not
                if self.player.get_score() > 21:
                    # this needs to do something though
                    is_player_not_bust = False
                    break
                
                self.display_current()
                user_input = self.available_options(bet_amount, is_first_time=False)

            # this part is messy, but basically it only runs if natural_blackjack() doesn't run
            if not_natural_blackjack:
                self.dealer.get_deck().hide_card(1, False)
                if is_player_not_bust:
                    # deals cards to dealer if their hand is below 17
                    if self.dealer.get_score() < 17:
                        print("Dealer is drawing cards...")
                        self.dealer_draw(blackjack_deck)
                        sleep(0.5)



                    print(f"Dealer score: {self.dealer.get_score()}") # prints the dealer's final score
                    self.display_current()
                    if self.dealer.get_score() > 21:
                        print("The dealer has bust")
                        print(f"You received {bet_amount * 2}")
                        self.player.add_money(bet_amount * 2)

                    elif self.player.get_score() ==  self.dealer.get_score(): 
                        print("Push!")
                        print(f"You received {bet_amount} back")
                        self.player.add_money(bet_amount)
                    
                    elif self.player.get_score() > self.dealer.get_score():
                        print(f"You received {bet_amount * 2}")
                        self.player.add_money(bet_amount * 2)

                    elif self.player.get_score() < self.dealer.get_score():
                        print("The dealer has a higher score")
                        print(f"You lost ${self.player.bet}")

                elif not is_player_not_bust:
                    self.display_current()
                    print(f"You lost ${self.player.bet}")


            # reset the round - this is ran every round
            not_natural_blackjack = True
            self.player.reset_bet()
            bet_amount = 0
            self.player.get_deck().reset_deck()
            self.dealer.get_deck().reset_deck()

            # finishes game if the player's balance is 0
            if self.player.get_money() == 0:
                print("You are out of money!")
                return 

        return



    


    


if __name__ == "__main__":

    a = Blackjack(5)
    a.main()



    