'''
Dictionaries - a data structure in python like lists, sets, and tuples that allows to interact with data in a certain way.
key-value pair = They are for associating keys and values together
If you know the key then you can access the value very easily
Example: A dictionary of your friends names being the keys and their ages being the values, therefore if you know the name of your friend you can get their age as well
'''

friendAges = {"Rakin": 29, "Faraz": 28, "Jack": 30}                             # A dictionary of 3 elements, where each element is a key-value pair
# the pairing is done with a colon, and the value '29' is associated with the string 'Rakin' as a key
# keys must be strings, integers, or any hashable types

# Accessing a particular element
print(friendAges["Rakin"])                                                               # Accesses Rakin's age and prints as 29
# Lists, tuples - subscript notation used to access particular index 
# Dictionaries - subscript notation won't work, you need to access the keys instead

# Add a particular element:
friendAges["Ben"] = 20
print(friendAges)

# Change a particular element:
friendAges["Ben"] = 25
print(friendAges)

# List of dictionaries - Example of a list of friends: each dictionary represents and describes a friend
friends = [
    {"name": "John", "age": 25},
    {"name": "Brenda", "age": 27},                                        
    {"name": "Sadiq", "age": 23}

]

# Accessing a list of dictionaries or a particular value inside it
print(friends)
print(friends[1])
print(friends[2]["name"])

# If you have a list of lists, you would access multiple indices in succession 
# If you have a dictionairy of dictionaries, you would access multiple keys in succession

studentGrades = {"John": 95, "Brenda": 86, "Sadiq": 100}

# iterate over a dictionary by using a for loop, which gives you the keys 
for student in studentGrades:
    print(f"{student}: {studentGrades[student]}%")

# Better way to access a dictionary in a for loop
for student, grades in studentGrades.items():       # studentGrades.items gives two values for each student that you get as two seperate variables in 'student' and 'grades'
    print(f"{student}: {grades}")


# 'In' keyword is used to check whether a value is one of the keys of the dictionary
if "Brenda" in studentGrades:                                           # "in" keyword checks only for keys in a dictionary, NOT the values
    print(f"Brenda: {studentGrades['Brenda']}")                         # Brenda's grade is: 
else:                                                                   # "Otherwise"
    print("Brenda didn't receive a grade yet")

# Getting ONLY the values back without worrying about the keys in a dictionary:

gradeValues = studentGrades.values()                        # creating a variable called gradeValues which contain all the values of studentGrades
print(sum(gradeValues) / len(gradeValues))                  # Adding 95, 86, 100 together and then dividing it by 3 which is the length of the list.


