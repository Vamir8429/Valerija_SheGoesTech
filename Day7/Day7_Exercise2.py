# 2. Palindrome

# Write the function is_palindrome(text)

# which returns a bool True or False depending on whether the 
# word or sentence is read equally from both sides.

# PS You can start with a one-word solution from the beginning, 
# but the full solution will ignore whitespace and uppercase and lowercase letters.

# is_palindrome ("Alus ari i ra    sula") -> True

# is_palindrome("ABa") -> True

# is_palindrome("nava") -> False

def is_palindrome(text):
    text = str(text)
    if text == text[::-1]:
        print("True")
    else:
        print("False")

text = "aba"
is_palindrome(text)
