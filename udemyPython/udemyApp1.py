user_age = input("Enter your age: ")    # Using input function to make a string ask for an input
years = int(user_age)                   # Allowing the string to be converted into an integer
months = years * 12                     # calculating amount of months from the input of years
print(f"Your age in {years} years is equivalent to {months} months")

# More simple form of the same code above^: (reason: so you don't have a variable only used as a temporary measure, before it gets converted into another type)
user_age = int(input("Enter your age:"))    # Putting input function inside int function to turn the user input into an integer
months = user_age * 12
print(f"Your age in {user_age} years is equivalent to {months} months")
