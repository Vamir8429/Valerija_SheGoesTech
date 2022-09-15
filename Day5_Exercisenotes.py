# 2. Almost Hangman

# Write a program to recognize a text symbol
# The user (first player) enters the text.
# Only asterisks instead of letters are output.
# Assume that there are no numbers, but there may be spaces.
# The user (i.e. the other player) enters the symbol.
# If the letter is found, then the letter is displayed in ALL the appropriate places, 
# all other letters remain asterisks.

# Example:

# First input: Kartupeļu lauks -> ********* *****
# Second input: a -> *a****** *a***

player_text = input("First player, please enter a text:")
print(player_text)
text_hided = "*"*len(player_text)
print(text_hided)

player_text_2 = input("Second player, please enter a symbol:")
print(player_text_2)

