"""
print('What is your name?')
name = input()                      # Receiving input from the user at the terminal
print('Your name is: ' + name)      # String Concatenation
"""


# Create your own text adventure game!
# Present 5 scenarios to a user and give them 2 options to choose from for each scenario.
# Make it fun! Create a story and have your character choose which way to go


# This game is a linear path for the thief

#Start
print('You are a theif walking the kings road. You come across an abandoned castle.')

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
        print('You broke open the lock and were poisoned by the gas in the chest. You died. The end')
    elif decision == 'move on':
        # Scenario 3
        print('You have come upon a trap! \n what do you do? \n Enter (cross it, look for another path)')
        decision = input()
            if decision == 'cross it':
                print('You have failed to cross the path, you died!')
            elif decision == 'look for another path':
                # Scenario 4
                print('You find another path which leads to a a door and an opening with a dark crevice! \n Which opening do you enter? \n Enter (Open door, enter crevice)')
                decision == input()
                    if decision == 'open door':
                        print('You see a room full of treasure! Hurrah you are rich! The end!')
                    elif decision == 'enter crevice':
                        print('You see a dragon, he farts and sneezes and the methane enflames the air aroud you. You explode!')

