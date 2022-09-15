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