#So the weekend exercise is as follows: # write a program that asks for two text inputs s1 and s2 
# you can use better names than s1 and s2

# then checks if all the characters in first string are in second string
# if they are, print All character counts in the second string
# if not, print Not all characters are in the second string
# example
# s1 = "abc"
# s2 = "abracadabra"
# output: a 5, b 2, c 1, d 1, r 2  # so do not print the empty ones

# example two
# s1 = "abc"
# s2 = "def"
# output: Not all characters are in the second string
# so preferably use alphabetic ordering  :)

text_1 = input("Enter your text: ")
text_2 = input("Enter another text: ")
print(text_1) #I had a great weekend
print(text_2) #I went to Klaipeda
check = text_1 in text_2 #check if all characters in text_1 are in text_2 - False 
if check == True:
    print("All character counts in the second string")
else:
    print("Not all characters are in the second string")

#text_1 = input(str("Enter your text: "))
#text_2 = input(str("Enter another text: "))
#print(text_1) #I had a great weekend
#print(text_2) #I went to Klaipeda

#for num in range(len(text_1)):
#    print(text_2.find("text_1[0]"))
