import random
import os
from utilityFunctions import validateInput, displayResult, printDefinition


# Getting the word from a different file called hangmanList.py
from hangmanList import wList

os.system('clear') # Clearing the screen for better reading

# To get a random word from the list, get a random integer
index = random.randint(0, len(wList)-1)
curWord = wList[index]

successChars = []
failedChars = set() #set to avoid duplicates

# Maximum attempt for this game is 6
remAttempt = 6
userWon = False
skip = False
maskedString = "_ " * len(curWord)

# Print the initial dashes which is the same length as the word chosen
displayResult(maskedString, remAttempt, failedChars)

# Let's keep the game going until the maximum attempts have reached or when the user has won the game
while remAttempt > 0 and not userWon:

    getChar = input("Guess the letter: ")
    getChar = getChar.lower()

    os.system('clear')

    # Perform basic validations of input character

    if getChar.upper() == "QUIT":
        break

    # validate the input character
    correctInput = validateInput(getChar, successChars, failedChars)

    if not correctInput:
        displayResult(maskedString, remAttempt, failedChars)
        continue

    if getChar in curWord: # Success
        successChars.append(getChar)
    else: # Fail
        remAttempt -= 1
        failedChars.add(getChar)

    maskWord = []

    # Construct the current masked-word
    for x in curWord:
        if x in successChars:
            maskWord.append(x)
        else:
            maskWord.append('_')

    maskedString = " ".join(maskWord) # Change the list into a string with a space

    displayResult(maskedString, remAttempt, failedChars)

    if curWord == maskedString.replace(' ', ''): # User won the game
        userWon = True
        print("")
        print("!!!! * * * YOU WON! * * * !!!!")

    elif remAttempt == 0: # User lost the game, all attempts were used
        print("")
        print("Hangman! :( YOU LOST ):")
        print("The word is " + curWord)

printDefinition(curWord)







