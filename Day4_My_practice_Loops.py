#print("Hello")
#print("Hello")
#print("Hello")
#print("Hello")

# we can use while loop to print the same line 5 times
# this can heat up the computer ...
# while True:
#     print("Do you want to continue?")
#CMD+C to stop program

#Infinite loop can be useful (used in games, applications)

i = 2  # so caller iterator, or index if you will
while i < 5:  # while loops are for indeterminate time
    print("Hello No.", i)
    print(f"Hello Number {i}")
#     # it is crucial that we increment the iterator
#     # otherwise we will get an infinite loop
    i += 1  # i = i + 1 # we will have a infinite loop without i += 1, there is no i++
# # while loop is finished here
print("Always happens once loop is finished")
print("i is now", i)
# #
#OUTPUT:
#Hello No. 2
#Hello Number 2
#Hello No. 3
#Hello Number 3
#Hello No. 4
#Hello Number 4
#Always happens once loop is finished
#i is now 5

i = 3
while i >= 0: #as soon as this is false, it stops running loop
    print("Going down the floor:", i)
# i could do more stuff
    if i == 0:
        print("Cool we reached the garage")
    i -= 2  # i = i - 1
print("Whew we are done with this i floor:", i)
# # #
#OUTPUT 
#Going down the floor: 5
#Going down the floor: 3
#Going down the floor: 1
#Whew we are done with this i floor: -1

print("End of example")

total = 0 # do not use sum as name for variable, because it is built in function 
i = 20
print(f"BEFORE loop i is {i} total is {total}")
while i <= 30:
    total += i # total = total + i
    print(f"After adding {i} total is {total}")
    i += 2 # step will be 2 here
print(f"i is {i} total is {total}")

#OUTPUT 
#BEFORE loop i is 20 total is 0
#After adding 20 total is 20
#After adding 22 total is 42
#After adding 24 total is 66
#After adding 26 total is 92
#After adding 28 total is 120
#After adding 30 total is 150
#i is 32 total is 150

print("End of example")

# # # general loop with start, stop, step
start = 50
stop = 400
step = 125  # we do have a for loop for this type of looping but step here can be a float
i = start  # initialization
while i <= stop:  # you could also stop before stop is reached then use  i < stop
    print(i)
    print(f"i is {i}")
    i += step
print("After exiting loop i is ", i)

#OUTPUT
#50
#i is 50
#175
#i is 175
#300
#i is 300
#After exiting loop i is  425

i = 10
while True:  # so i am saying here that this loop should run forever .. unless I have something inside to break out
    print("i is", i)  # this line will always happen at least once
## could add more lines which will run at least once
#in a while True loop it is typical to check for exit condition
    if i >= 14:  # similar to while i < 28:
        print("Ready to break out i is", i)
        break  # with break we break out of loop
    i += 2
# # # above is simulating do while looping functionality
print("Whew AFTER BREAK out", i)
# # #

#OUTPUT 

#i is 10
#i is 12
#i is 14
#Ready to break out i is 14
#Whew AFTER BREAK out 14

#above example is do while loop 
#do while loops do something at least once and check for exit condition 
#shoot first and ask questions later 

i = 20
is_active = True  # we will use this as a flag
is_raining = True
#while active or is_raining:  # careful here so for while loop to keep running here JUST ONE of the conditions here have to be true
while is_active and is_raining:  # so for while loop to keep running here BOTH conditions here have to be true
    print(f"Doing stuff with {i}")
    i += 3
# TODO update weather conditions so update is_raining
    if i > 30:
        is_active = False
        #I could have used break as well
    # with flag set I can still do some work here
# # # #

#Doing stuff with 20
#Doing stuff with 23
#Doing stuff with 26
#Doing stuff with 29

#so break exits the loop
#continue goes back to the start of the loop (without finishing the current iteration/cycle)

while True:
    res = input("Enter number or q to quit ")
#     if res.lower().startswith("q"): # more lenient any word starting with Q or q will work to quit
    if res == "q":
        print("No more calculations today. I am breaking out of the loop.")
        break
    elif len(res) == 0:  # so i had an empty string here...
        print("Hey! You just pressed Enter, please enter something...")
        continue # we go back to line 83 and start over
    # elif res == "a":  # TODO check if if the input is text
    elif res[0].isalpha():  # we are checking here for the first symbol of our input
        print("I can't cube a letter ")
        continue # means we are not going to try to convert "a" to float
        # in other words we are not going to do the below 4 instructions
    num = float(res)
    cube = num**3
    cube = round(cube, 2) # 2 digits after comma
    print(f"My calculator says cube of {num} is {cube}")
# # #
print("All done whew!")

#Enter number or q to quit 5
#My calculator says cube of 5.0 is 125.0

#Enter number or q to quit Q
#I can't cube a letter 

#So while loops are best suited for looping when we do not know the exact number of loops


