# List comprehensions-------------------------------------------------------------------
# Iteration means the repetition of a process or utterance.
# Append means to add something to a new list, tuple, or set

# Example of code without List comprehension
numbers = [1, 3, 5]
doubled = []

for num in numbers:                       # iterates over 'numbers list', and creates a new variable in 'num' for each of the elements in the 'numbers list' (Iterating)
    doubled.append(num * 2)               # runs through the code 3x, each time putting the appropriate # multiplied by 2 into a new list (Appending)

print(doubled)

# Example of code with List comprehension 
numbers = [2, 4, 6]
doubled = [num * 2 for num in numbers]                  # puts 'num * 2' into a new list, for the variable 'num' in the 'numbers list'
# iterating over the 'numbers list', & putting the variable 'num' multiplied by 2 everytime that the loop runs into a new list, and ending up with the doubled numbers

print(doubled)

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Create a new list with the friends that start with an R

# Without List comprehension
friends = ["Rakin", "Jack", "Robert", "Ben", "Randy"]
startsWithR = []                                                        # the new list that will have the names that start with the letter specified

for friend in friends:                                                  # creates new variable 'friend', for each of the elements in 'friends list' in the 'for loop'
    if friend.startswith("R"):                                          # .startswith method returns true if the string starts with specified value in the 'if statement'
        startsWithR.append(friend)                                      # runs through the code 5x, each time putting the appropriate name into a new list by 'append'

print(startsWithR)                                                      # prints names only starting with R without list comprehension

# With List comprehension and does the same thing as the code above.
friends = ["Rakin", "Jack", "Robert", "Ben", "Randy"]
startsWithR = [friend for friend in friends if friend.startswith("R")]                      # Adding a conditional or if statement to a list comprehension
# Code breakdown:
# First, you put what you want to add to your new list which is : a 'friend' name
# Next, you put your for loop or iteration which is: for friend in friends
# Lastly, you add your if statement which is: if friend.startswith("R")

print(startsWithR)                                                      # prints names only starting with R with list comprehension
print(friends)                                                          # prints all names
print(friends is startsWithR)                                           # prints false because although the two lists have the same contents, they are NOT the same list
print(friends[0] is startsWithR[0])                                     # prints true because the exact elements inside the two lists when compared are the same
print(friends[0] is startsWithR[1])                                     # prints false because the exact elements inside the two lists when compared are different


# Checking with IDs: The ID is related to the memory address in which the list is stored---------------------------------------------------------------------------

# When two lists are different
friends = ["Rakin", "Jack", "Robert", "Ben", "Randy"]
startsWithR = [friend for friend in friends if friend.startswith("R")]   

print("friends: ", id(friends), "statsWithR: ", id(startsWithR))        # The IDs are different so when compared with 'is' it will print false
print(friends is startsWithR) 

# Making two lists the same thing
friends = ["Rakin", "Jack", "Robert", "Ben", "Randy"]
startsWithR = friends  

print("friends: ", id(friends), "statsWithR: ", id(startsWithR))        # The IDs are same so when compared with 'is' it will print true
print(friends is startsWithR) 

# Conclusion: Creating new lists gives you a different thing entirely in python, its NOT the same as the thing before, even if it has the same contents


