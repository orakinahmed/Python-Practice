# Booleans - a value that's either true or false, created by using comparisons to compare two things together to calculate if they're the same or different
# one '=' sign is used to assign a value to a variable, two '==' sign are used to compare two things.

print(5 == 5)   # 5 is 'equal to' 5 so prints true

print(5 > 5)    # 5 is not 'greater than' 5 so prints false

print(10 != 10) # 10 'is not' different than 10 so prints false

# Comparisons: ==, !=, >, <, >=, <=

friends = ["Rakin", "Faraz"]
abroad = ["Rakin", "Faraz"]
print(friends == abroad)        # '==' compares whether the elements inside the lists are the same, since comparing two strings in this example, this prints true
print(friends is abroad)        # 'is' compares whether two lists are the same thing, each list in this example has its own area in memory, so this prints false
print(friends is friends)       # friends list are the same lists, so this prints true

# 'is' keyword checks elements inside the list were created seperately and they could be the same between both lists, BUT the lists themselves are different
# in short 'is' keyword checks whether two elements are EXACTLY the same thing, not whether they have the same elements inside them or whether they're similar
# '==' is preferred over the use of 'is'


# If statements-----------------------------------------------------------------------------------------------------------------------------------------------------
dayOfWeek = input("What day of the week is it today? ").lower()             # .lower() allows the user to input days of the week in any case (upper/lower) 

#check if the day of the week is monday
if dayOfWeek == "monday":                           # if this is true run the code and print the statement attached
    print("Have an amazing start to your week!")
elif dayOfWeek == "tuesday":                        # elif allows you to add branches to your if statement 
    print("It's Tuesday!")
elif dayOfWeek == "wednesday":
    print("It's Wednesday!")
elif dayOfWeek == "thursday":
    print("It's Thursday!")
elif dayOfWeek == "friday":
    print("Have a great weekend!")
else:                                               # otherwise run this code if neither 'if' and 'elif' are true, and print the statement attached
    print("Thank god it's the weekend!")         

# The order of keywords: 'if' comes first, 'elif' comes next, 'else' comes last. 
# 'elif' and 'else' are optional to the overall if statement, and used when needed. 

print("This line runs regardless irrespective to the code with the if/else statement")


# "In" keyword is used to check for membership: whether one thing is inside a list, tuple, or set -----------------------------------------------------
friends = ["Rakin", "Faraz", "Ali"]
print("Ali" in friends)

watchedMovies = {"Avengers", "Thor", "Hulk" }
userMovie = input("Enter a movie you've watched: ")

print(userMovie in watchedMovies)           # If input is true prints true.

# If statements with 'in' keyword
if userMovie in watchedMovies:
    print(f"I've watched {userMovie} too!")
else:
    print(f"I haven't watched {userMovie} yet.")

