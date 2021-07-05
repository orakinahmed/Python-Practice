#for i in range(0, len(data)):
    #stuff that happens inside loop

# TODO #1
# Create an array with 5 items  
# Loop through them
# Print out the items to console

teams = ['falcons', 'bucs', 'saints', 'panthers', 'titans']
for counter in range(0, len(teams)):
    print(teams[counter]) 


for team in teams:
    print(team)


# TODO #2
# Create a function multiply() that takes in two arguments and multiplies them. 
# Call the function
# Print the result

"""
public int multiple(num1, num2) {
    int result = num1 * num2;
    return result;
}

int result = multiply(7,5);
"""

def multiply(num1, num2):
    result = num1 * num2
    return result

result = multiply(7,5)
result = 100
print(result)


# TODO #3
# Create a dictionary with 4 keys age, name, height, color
# Print the person's name
# Loop through dictionary and print each key

player = {'age': 20, 'name': 'bob', 'height': 73, 'color': 'brown'}
print(player['name'])


for key in player:
    print(key)


def newPlayer():
    player =  {'age': 20, 'name': 'bob', 'height': 73, 'color': 'brown'}
    return player

player = {'age': 99, 'name': 'chuck', 'height': 73, 'color': 'white'}
player = newPlayer()

print(player)


def printNames():
    for i in range(0,5):
        print('sally')

printNames()

product = multiply(8, 4)
print(product)


# WHen you call a function by its name you are asking it to run its code
# When a function returns you need to do something with it

"""
public static void sayMyNameBitchFiveTimes() {
    for (int i=0; i<5; i++) {
        System.out.println('faraz');
    }
}
"""

def sayMyNameBitchFiveTimes():
    for i in range(0,5):
        print('faraz')

name = sayMyNameBitchFiveTimes()
print(name)