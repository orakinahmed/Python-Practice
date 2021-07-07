"""
OOO - Object Oriented Programming

What is an object?
Class/ Object - A blueprint for a series of tasks (functions) and types of data (properties)
Object is one version of a class
Every class has properties. Every class has functions
_________________________________________________
"""

"""
Ex. Creating a class
House -> Object
- color         -> Properties
- material 
- price

Functions ->
    def getColor() -> Retreives the color
    def setColor() -> Update the color of the house
_________________________________________________
"""

"""
Ex. Using Objects

rakin = House()
rakin.setColor('Blue')
rakin.getColor()

faraz = House()
faraz.getColor()
_________________________________________________
"""

"""
Ex. Flask
from flask import Flask

app = Flask(__name__)

app.route()
app.run()

documentApp = Flask(__name__)
_________________________________________________
"""


"""
Arrays - To store items in a list
Dictionary - To store items via a key and value pair
If Statments - Conditions
For Loops | While Loops - Repetition Tasks
Functions - To perform a task and reuse it

Classes - To represent a blueprint of tasks and data
"""


# What is my class or my blueprint
class Car():

    # Intializer function
    def __init__(self, year, make, model, color):
        self.year = year
        self.make = make
        self.model = model
        self.color = color

    # Getters & Setter Functions
    def getYear(self):
        return self.year

    def setYear(self, year):
        self.year = year


# --------------------------------

if __name__ == '__main__':
    print('Testing')

    car1 = Car('1968', 'Honda', 'Civic', 'Black')
    print(car1.getYear())
    car1.setYear('1945')
    print(car1.getYear())