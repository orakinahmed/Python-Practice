"""
print('What is your name?')
name = input()                      # Receiving input from the user at the terminal
print('Your name is: ' + name)      # String Concatenation
"""


# Create your own text adventure game!
# Present 5 scenarios to a user and give them 2 options to choose from for each scenario.
# Make it fun! Create a story and have your character choose which way to go

def runTrapScenario(sword):
    # Scenario 3
    print('You have come upon a trap! \n what do you do? \n Enter (cross it, find another way)')
    decision = input()
    if decision == 'cross it':
        print('You have failed to cross the path, you died!')
    elif decision == 'find another way':
        # Scenario 4
        print('You find another path which leads to a a door and an opening with a dark crevice! \n Which opening do you enter? \n Enter (open door, enter crevice)')
        decision = input()
        if decision == 'open door':
            print('You find a room full of angry dogs. They eat you. The end!')
        elif decision == 'enter crevice':
            # Scenario 5
            if sword:
                print('You see a dragon, and kill it with the sword! You are heavily wounded.')
                return True
            else:
                print('You see a dragon, he farts and sneezes and the methane enflames the air aroud you. You explode!')
                return False



#Start
print('You are a thief walking the kings road. You come across an abandoned castle.')

# Scenario 1
print('Would you like to enter? \n Enter (yes or no)')
decision = input()
if decision == 'no':
    print("You went back home! The adventure ended!")
elif decision == 'yes':
    # Scenario 2
    print('You have entered the castle, and come upon a locked chest, what do you do? \n Enter (pick lock , move on)')
    decision = input()
    if decision == 'pick lock':
        print('You broke open the lock and found a sword. You put the sword on your waist, and moved on')
        survival = runTrapScenario(True)
        if survival == True:
            print('You get out the castle and follow another path to your homeland for your family')
    elif decision == 'move on':
        survival = runTrapScenario(False)
        if not survival:
            print('You became a ghost and exist haunting the afterlife for years to come!')
