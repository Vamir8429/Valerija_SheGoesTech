# 1. Confusion

# The user enters a name.
# You print user name in reverse (should begin with capital letter)
#  then extra text: ",a thorough mess is it not ", then the first name of the user name then "?"
# Example:
# Enter: Valdis -> Output: Sidlav, a thorough mess is it not V?

n = str(input("What is your name?"))
print("Thanks for the input " + n)
rev_n = n[::-1]
print(rev_n + " - This is your name in reverse order")
cap_n = rev_n.capitalize()
print(cap_n + " , a thorough mess, is it not? " + n[0])

# 3. Text conversion

# Write a program for text conversion
# Save user input
# Print the entered text without changes

# Exception: if the words in the input are not .... bad, 
# then the output is not ...  bad section must be changed to is good

text = input("Enter Your text, tell me about today's weather?")
print(text) #Weather is very bad
term_1 = "not"
term_2 = "bad"

find_1 = text.find(term_1)
find_2 = text.find(term_2)
replace = "good"

if 0 < find_1 < find_2:
    text = text.replace(text[find_1:(find_2 + len(term_2))], replace)
elif 0 < find_2:
    text = text.replace(text[find_2], replace)
print(text)


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

# no idea what to do next 

#Valdis solution: 

word = input("First player, enter the text: ")
# word = "Kartupeļu lauks"

#guessed = "".join("*" for char in word) # downside is that this will include the empty space
guessed = "*"*len(word) # same as above
letter = " "  # to add back the spaces before starting
#
while not letter == "0":
    # for i in range(len(word)):
    for i, c in enumerate(word): # more Pythonic
        # if word[i].lower() in letter.lower():  # guesses are not case sensitive
        if c.lower() in letter.lower():  # guesses are not case sensitive
            guessed = guessed[:i] + word[i] + guessed[i + 1:]

    if guessed.find("*") == -1:
        print("Good job!")
        break

    print(guessed)
    letter = input("Player 2: Guess a letter (or input 0 to give up): ")

print(f"The word is: {word}")