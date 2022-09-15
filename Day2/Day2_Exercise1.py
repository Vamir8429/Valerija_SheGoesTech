# 1. Exercise - Age 100

#
# Write a program that asks for and saves a username
# Ask a question about the user's age, using the username in the question.
# Shows in how many years the user will be 100 years old smile
# BONUS: then you will need two additional lines:
# import datetime # let's talk about imports separately
# currentYear = datetime.datetime.now (). year
# Let the program also show the year when the use will be 100 years old
# It could use a variable with the current year automatically 

username = input("What is your username?")
age = int(input(f"{username}, How old are you?"))
age_goal = 100
years_left = age_goal - age
print(years_left, "years left till 100 😀")
import datetime
currentYear = datetime.datetime.now (). year
year_goal = currentYear + years_left
print(f"{username}, in {year_goal} you will reach your goal of {age_goal}")

## my output i got: 
## What is your username?Vamir8429
## Vamir8429, How old are you?27
## 73 years left till 100 😀
## Vamir8429, in 2095 you will reach your goal of 100