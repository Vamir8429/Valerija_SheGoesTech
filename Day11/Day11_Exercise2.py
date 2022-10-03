# 2. Deck - probably for homework, see how far you get
# write a class Deck with the following attributes(variables)
# available - contains list of card tuples that can be used
# spent - contains list of card tuples that have been used

# there should be following methods:
# constructor (__init__) method
# initializes available with full 52 card list of tuples
# initializes spent with empty list

# shuffle(self):

# # shuffles available cards - works just like 1st function but works on available

# get_cards(self, count=1):
# # gets some number(default 1) of cards from available 
# adds these cards to spent
# returns these cards

# # you can add other methods and/or attributes if you wish to Deck class
import random
import string
import itertools

def get_shuffled_cards():
    my_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    my_cards = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
    cards = [(value, suit) for value in my_values for suit in my_cards]
    random.shuffle(cards)
    return cards

class Deck:

    my_cards = ["clubs (♣)", "diamonds (♦)", "hearts (♥)", "spades (♠)"]
    my_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    def __init__(self):
        self.available = list(itertools.product(self.my_values, self.my_cards))
        self.shuffle()
        self.spent = []

    def __str__(self):
        return f"Available cards: {self.available}\nSpent cards: {self.spent}"

    def shuffle(self):
        self.available = random.sample(self.available, len(self.available))
        return self

    def get_cards(self, count=1):
        cards = self.available[:count]
        self.spent.extend(cards)
        self.available = self.available[count:]
        return cards

if __name__ == "__main__":
    print(get_shuffled_cards())
    my_deck = Deck()
    my_deck.shuffle()
    print(my_deck)
    print(my_deck.get_cards(2))
    print(my_deck.get_cards(6))
    print(my_deck)
