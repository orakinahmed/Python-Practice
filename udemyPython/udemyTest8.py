# Functions in Python
# def keyword is used to create or define a function, then put a name for the function you want to define it with, followed by brackets, and a colon
# "when you define a function you create a callable variable"

def hello():            # hello becomes a callable variable whose value is a function (a function you can call, run, or execute)
    print("Hello!")     # indentation allows you to place lines within the function

# Creating or defining a function does not run the function body, it just tells python that a variable (by its name: "hello") exists

hello()                 # the variable name of the function followed by brackets calls the function and executes it 


def userAgeInSeconds():
    userAge = int(input("Enter your age: "))
    ageSeconds = userAge * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {ageSeconds}.")

userAgeInSeconds()




