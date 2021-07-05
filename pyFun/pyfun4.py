
#-----------------------CODING FOUNDATIONS 

# Looping from 0 to end of an array | Repeating code i times
arr = []
for i in range(0, len(arr)):
    pass # do something

# Looping over an array | Repeating code for however many items in array
for item in arr:
    pass # do something

# If Statements | Conditional statments that compare one side to another. 
# Use == insteaf of = to compare
    if name == 'faraz':
       pass # do something

# Functions - A block of code that does something.

def sum():
    total = 5 + 2 

sum()       # To use a function you must call it by its name

#-------------------------BASIC DATA STRUCTURES

# Array - A list of items of any type (int, string, dictionary, etc.)
names = ['faraz', 'bob', 'joe']
names[1]           # Access items in Array by its INDEX

# Dictionary - A collection of one OR more key value pairs in {}
students = {'name': 'Faraz', 'age': 12, 'sex':'male'}
students['age']    # Access items in Dictionaries by its KEY

# ----------------------------------------------------------------

# 1) Create a loop that prints out hey 5 times and a seperate message that says what number of loop its on
for i in range(0, 4):
    print('hey')
    print('You are on loop' + str(i))

# 2) Create a loop that loops over an array of 5 items and prints out each item in the array
items = ['faraz','rakin','bob','jane','ben']

for i in range(0, len(items)):
    print(items[i])

for item in items:
    print(item)

# 3) Create a loop that loops over a dictionary with 5 key: value pairs, and prints each value
nfl = {'team': 'falcons', 'city': 'atlanta', 'division': 'nfc south', 'state': 'GA', 'country': 'USA'}

for item in nfl:
    print(nfl[item])


# 4) Create a variable called weight1, weight2 and do an if statement to see who is heavier and then print that person.
weight1= 150
weight2= 180

if weight1 > weight2:
    print('weight1 is heavier')
elif weight2 > weight1:
    print('weight2 is heavier')
else:
    print('no one is heavier')

# 5) Create a loop that loops over an array of 3 names (the second name is 'faraz'). Print which index faraz is located
names = ['rakin', 'faraz', 'jack', 'faraz'] 

for i in range(0, len(names)):
    if names[i] == 'faraz':
        print(i)