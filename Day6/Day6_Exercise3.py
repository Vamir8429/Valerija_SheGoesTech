# 3. Reversed words

# The user enters a sentence.

# We output all the words of the sentence in a reverse form. 
# - not the whole text reversed!!

# Example

# Alus kauss mans -> Sula ssuak snam
# notice how each word was reversed separately

# PS Split and join operations could be useful here.

sentence = input("Enter the sentence: ") #I love you 
print(sentence, "-This is your entered text")
words = sentence.split(" ")
print(words[::-1], "-This is your sentence in a reverse order")
sentence_again = " ".join(words[::-1])
print(sentence_again)
