#Loops------------------------------------------------------------------------------------------------------------------------------
'''
There's 2 types of loops (for/while):
1. One that allows us to repeat some code a certain # of times
2. One that allows us to repeat code for as long as a condition is true
'''

# Example of a while loop:
magicNumber = 5                                                                              
   
while True:                                                                         # Creates an infinite loop
    userInput = input("Would you like to play a game? (Y/n) ")   

    if userInput == "n":                                                            # if the user types 'n' the code terminates, if they type something else, it continues
        break                                                                       # break keyword allows us to exit a loop and continues our code on the next line

    userNumber = int(input("Please enter a number between 1-10: "))
    if userNumber == magicNumber:
        print("You have guess the number correctly!")
    elif abs(magicNumber - userNumber) == 1:
        print("You are off by one number!")
    else:
        print("Sorry, that number is wrong!")

# Example of a for loop:
friends = ["Rakin", "Faraz", "Shajid", "Jose"]          # Has 4 elements within this list so the for loop will run 4 times

# for friend in range(4):                               # runs a loop 4 times when you don't have a list of 4 elements
for friend in friends:                                  # 'for' keyword allows you to define a variable that will take the first value of the list its 'in'
    print(f"{friend} is my friend")                     # the code will repeat itself for the first, second, third, & fourth values until it reaches the end of the loop

# use a for loop to calculate the average grade of this class
grades = [35, 67, 98, 100, 100]
total = 0 
amount = len(grades)

# use a for loop to modify the total variable and to add to it each of the grades
for grade in grades:                                    # 'for' grade creates a new variable for grade, and helps us go through each of the values in the grades list
    total += grade                                      # same as ---> total = total + grade (adds up the existing total plus the new grade and sets it back to total)

print(total/amount)

# Alternate code for grades without a for loop
grades = [35, 67, 98, 100, 100]                         # a list of grades
total = sum(grades)                                     # sum calculates the addition of all the elements inside a list, tuple, or set
amount = len(grades)                                    # len calculates the length of a list

print(total / amount)

# Tip = how to search in google for the code above: "How to add a list of numbers in python?""

# Coding Exercise 3: Floq Control---loops and ifs

# -- Part 1 -- 
# Modify the code so that the 'evens list' contains only the even numbers of the 'numbers list'
# Only append the numbers that are even
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

evens = []
for number in numbers:
    if number % 2 == 0:                 # modulus operator: '%' ---> gives us the remainder of the division, therefore if the # / 2 has no remainder then this line is 0
        evens.append(number)            # appending every number in the 'numbers list' to the 'evens list'
print(evens)

# -- Part 2 --
# Add a clause to the if statement such that if the user's input is "q", your program prints "Quit"
user_input = input("Enter your choice: ")
if user_input == "a":                   # if the user input is 'a' were not going to check whether its 'q'
    print("Add")
elif user_input == "q":                 # elif used because user input will never be both 'a' and 'q' at the same time
    print("Quit")

