# Destructuring Variables

x = 5, 11                       # tuple with two values
x, y = 5, 11                    # a destructured tuple where python assigns two variables seperately: x to 5 and y to 11 

t = 7, 12                       
x, y = t
print(x)
print(y)
print(x, y)

# destructuring tuple into student and grade:

studentGrades = {"Randy": 75, "Sandy": 85, "Mandy": 95}

for student, grade in studentGrades.items():                        # iterating over studentGrades.items
    print(f"{student}: {grade}")


# modified code: prints a list of tuples:

studentGrades = {"Ren": 75, "Ben": 85, "Jen": 95}

print(list(studentGrades.items()))


# modified code: Accessing components instead of t, by destructuring into two seperate variables 

studentGrades = {"Rex": 75, "Lex": 85, "Sex": 95}

for t in studentGrades.items():
    print(t)


# List of people, where each person has a tuple with three values: their name, age, and profession

people = [("Bob", 23, "Engineer"), ("Rob", 34, "Doctor"), ("Fob", 27, "Chef")]

for name, age, profession in people:                              # iterates through each of the tuples and for each one, destructures it, into its three seperate components 
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# Alternative: (code above looks nicer because of destructuring)   
for person in people:                                                         # iterates over each tuple and prints out each thing using indices 
    print(f"Name: {person[0]}, Age: {person[1]}, Profession: {person[2]}")    


# Extraction of a single tuple 
person = ("Dood", 99, "Stripper")
name, _, profession = person                                # extracting person's name and profession without caring for age (underscore is used when ignoring a variable)

print(name, profession)


# how to seperate a list of 5 elements into two lists
# can only put asterisk for one of the variables

head, *tail = [1, 2, 3, 4, 5]                               # first value becomes the head, the rest of the values are collected and put into *tail because of the asterisk
print(head)
print(tail)
