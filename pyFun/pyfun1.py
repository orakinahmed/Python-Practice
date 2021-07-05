
"""
    # iterator or counter
    for i in range(0, len(students)):
        System.out.println('hey');
    }

    i = 0 | "hey" | 0 < 2 | -> 1
    i = 1 | "hey" | 1 < 2 | -> 2
    i = 2 | 2 < 2
"""

# Create a array of 2 students
# Each student needs to be a dictionary with name, age, color, weight, height, gpa

students = [
    {'name': 'rakin', 'age': 29, 'color': 'brown', 'weight': 200, 'height': 70, 'gpa': 5.0},
    {'name': 'faraz', 'age': 28, 'color': 'red', 'weight': 150, 'height': 80, 'gpa': 6.0}
]

# Name Student 1
studentName = students[0]['name']

# Weight Student 1
studentWeight = students[0]['weight']

# Student 2 Color
studentColor = students[1]['color']


print(studentName)
print(studentWeight)
print(studentColor)


# Make a function called heaviest that returns the heaviest student | Output that child's name to terminal with a message

def heaviest():
    
    heaviestWeight = 0
    heaviestStudent = ''

    for i in range(0, len(students)):

        if students[i]['weight'] > heaviestWeight:
            heaviestWeight = students[i]['weight']
            heaviestStudent = students[i]['name']

    return heaviestStudent

name = heaviest() # Calling a function | or using a function

print('The heaviest child is: ' + name)