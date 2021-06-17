from random import shuffle

class Card:
    def __init__(self, rank, suit, hidden=False):
        self.rank = rank
        self.suit = suit
        self.hidden = hidden


    def set_hidden(self, bool):
        self.hidden = bool

    
    def __str__(self):
        return f"{self.rank}{self.suit}"

    def get_rank(self):
        return self.rank


    def ascii(self):
        if self.suit == "S":
            ascii_suit = "♠"
        elif self.suit == "H":
            ascii_suit = "♥"
        elif self.suit == "C":
            ascii_suit = "♣"
        elif self.suit == "D":
            ascii_suit = "♦"
        else:
            ascii_suit = self.suit

        if len(self.rank) < 2:
            ascii_rank = self.rank + " "
        else:
            ascii_rank = self.rank

        if not self.hidden:
            card_ascii = [
                '┌───────┐',
                f'|{ascii_rank}     |',
                '|       |',
                f'|   {ascii_suit}   |',
                '|       |',
                f'|     {ascii_rank}|',
                '└───────┘'
            ]
        else:
            card_ascii = [
            '┌───────┐',
            '|░░░░░░░|',
            '|░░░░░░░|',
            '|░░░░░░░|',
            '|░░░░░░░|',
            '|░░░░░░░|',
            '└───────┘'
        ]

        return card_ascii




class Deck:
    def __init__(self):
        self.cards = []

    def deck_length(self):
        return len(self.cards)

    def reset_deck(self):
        temp = self.cards
        self.cards = []
        return temp


    def get_cards(self):
        return self.cards


    def generate_standard(self):
        ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        suits = ("D", "C", "H", "S")
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))


    def add_card(self, rank, suit, hidden=False):
        for card in self.cards:
            if rank == card.rank and suit == card.suit:
                print("The card is already in the deck")
                break
        self.cards.append(Card(rank, suit, hidden))
    
    
    def draw_card(self):
        try:
            return self.cards.pop()
        except IndexError:
            print("You cannot draw a card from an empty deck")


    def shuffle(self):
        shuffle(self.cards)

    
    def display_vertical(self):
        display_list = [card.ascii() for card in self.cards]
        for card in display_list:
            for row in card:
                print(row)


    def display_horizontal(self):
        display_list = [card.ascii() for card in self.cards]
        ASCII_ROW = 7
        for i in range(ASCII_ROW):
            for card in display_list:
                print(card[i], end =" ")
            print()


    def hide_card(self, index, hidden):
        self.cards[index].set_hidden(hidden)


if __name__ == "__main__":
    # for row in Card("A", "S").ascii():
    #     print(row)
    # a_deck = Deck()
    # a_deck.generate_standard()
    
    # def display_card():
    #     j = 0
    #     while j < (52 -3 ):
    #         for i in range(7):
    #             print(a_deck.cards[j].ascii()[i], a_deck.cards[j+1].ascii()[i], a_deck.cards[j+2].ascii()[i], a_deck.cards[j+3].ascii()[i])
    #         j += 4
    
    # display_card()
    
    # if input("Shuffle? ") == "y":
    #     a_deck.shuffle()

    # display_card()
    a_deck = Deck()
    a_deck.add_card("J", "S", True)
    a_deck.display_horizontal()
    a_deck.add_card("10", "D")
    a_deck.display_horizontal()
    a_deck.hide_card(0, False)
    a_deck.display_horizontal()
    a_deck.add_card("3", "D")
    a_deck.display_horizontal()
    a_deck.hide_card(2, True)
    a_deck.display_horizontal()

    


