# Create a magic number app (vid18)
# Decide on a magic number - a hidden number from the user, ask the user to enter a #, and then tell the user whether they got the number right.

''' 
Psedocode:
1. Ask the user if they want to play the game.
2. Decide on a magic number - create a variable which is hidden from the user. 
3. Ask the user to enter a #
4. Tell the user whether they got the number correct.
'''

magicNumber = 5                                                                              # Create a magic number
userInput = input("Would you like to play a game? Enter to 'yes' begin: ").lower()           # Asking the user if they want to play a game

if userInput in ("yes", "Yes", "y", "Y"):                                                    # preferred ------> if userInput == "y":
    userNumber = int(input("Please enter a number between 1-10: "))
    if userNumber == magicNumber:
        print("You have guess the number correctly!")
    elif magicNumber - userNumber in (1,-1):                                                 # preferred ------> abs(magicNumber - userNumber) == 1
        print("You are off by one number!")
    else:
        print("Sorry, that number is wrong!")


