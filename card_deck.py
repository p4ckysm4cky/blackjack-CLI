class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        return f"{self.rank}{self.suit}"

    def ascii(self):
        card_ascii = [
            '┌───────┐',
            f'|{self.rank}      |',
            '|       |',
            f'|   {self.suit}   |',
            '|       |',
            f'|      {self.rank}|',
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



if __name__ == "__main__":
    for row in Card(1, 2).ascii_hidden():
        print(row)


