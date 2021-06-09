from random import shuffle

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    
    def __str__(self):
        return f"{self.rank}{self.suit}"


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

        card_ascii = [
            '┌───────┐',
            f'|{ascii_rank}     |',
            '|       |',
            f'|   {ascii_suit}   |',
            '|       |',
            f'|     {ascii_rank}|',
            '└───────┘'
        ]
        return card_ascii


    def ascii_hidden(self):
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


    def get_cards(self):
        return self.cards


    def generate_standard(self):
        ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        suits = ("D", "C", "H", "S")
        for rank in ranks:
            for suit in suits:
                self.cards.append(Card(rank, suit))
    
    
    def shuffle(self):
        shuffle(self.cards)



if __name__ == "__main__":
    # for row in Card("A", "S").ascii():
    #     print(row)
    a_deck = Deck()
    a_deck.generate_standard()
    for j in range(52 - 3):
        for i in range(7):
            print(a_deck.cards[j].ascii()[i], a_deck.cards[j+1].ascii()[i], a_deck.cards[j+2].ascii()[i], a_deck.cards[j+3].ascii()[i])
    
    if input("Shuffle? ") == "y":
        a_deck.shuffle()

    for j in range(52 - 3):
        for i in range(7):
            print(a_deck.cards[j].ascii()[i], a_deck.cards[j+1].ascii()[i], a_deck.cards[j+2].ascii()[i], a_deck.cards[j+3].ascii()[i])
    


