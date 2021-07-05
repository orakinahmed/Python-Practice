# Create a array of 2 students
# Each student needs to be a dictionary with name, age, color, weight, height, gpa

students = [{'name': 'sam', 'age':'25', 'color': 'red', 'weight': 150, 'height': 178, 'gpa': 3.0},
            {'name': 'ben', 'age':'27', 'color': 'blue', 'weight': 160, 'height': 183, 'gpa': 3.5}



            ]




# Name Student 1 and print
studentName = students[0]['name']
print(studentName)



# Weight Student 1 and print 
studentWeight = students[0]['weight']
print(studentWeight)


# Student 2 Color and print
studentColor = students[1]['color']
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

    

    print(heaviestStudent)


