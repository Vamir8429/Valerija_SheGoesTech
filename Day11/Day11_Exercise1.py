# 1. The Shuffle

# write  a function get_shuffled_cards()

# Inside the function create  a 52-card list of tuples [("2", "diamonds ♦"), ("2", "hearts ♥"), ....., ("A", "spades ♠"), ("A", "clubs ♣")]

# The function returns a shuffled set of cards - the same list with tuples but shuffled!

# Find the correct method from built in random library.

# you can use a loop or use something from the library

# BONUS: Something can be useful from here: https://docs.python.org/3/library/itertools.html

import random

def get_shuffled_cards():
    my_values = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    my_cards = ["diamonds ♦", "hearts ♥", "spades ♠", "clubs ♣"]
    cards = [(value, suit) for value in my_values for suit in my_cards]

    random.shuffle(cards)
    return cards

if __name__ == '__main__':
    cards = get_shuffled_cards()
    print(cards[:5])

#OUTPUT:
#[(7, 'spades ♠'), (2, 'diamonds ♦'), (10, 'spades ♠'), (3, 'clubs ♣'), (10, 'clubs ♣')]