from PyDictionary import PyDictionary

def validateInput(inputChar, successChars, failedChars):

    validInput = True

    if len(inputChar) > 1:
        print("Enter one letter please")
        validInput = False

    elif not inputChar.isalpha():
        print("Enter only alphabet please")
        validInput = False

    elif inputChar in successChars or inputChar in failedChars:
        print(inputChar + " is already entered")
        validInput = False

    return validInput



def printHangman(stage):

    hangmanStages = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

    return hangmanStages[stage]

def displayResult(maskedString, remAttempt, failedChars):
    print("")
    print(" " * 20, "Hangman!")
    print("")
    print(" " * 20, "Guess the word: ", maskedString)
    print(printHangman(6 - remAttempt))
    print ("Remaining Attempt: " + str(remAttempt) + ",   Failed Characters = {" + ", ".join(failedChars) + "}")

def printDefinition(word):
    print("")
    print("Definition of " + word + ": ")

    # I use the PyDictionary library to look up the definitions of the word.
    # The "meaning" function of PyDictionary returns a dictionary object with
    # categories as key and list of definitons as values
    # I loop through the definitions and format it nicely and print it.
    dict = PyDictionary()
    meaning = dict.meaning(word)

    if meaning is None:
        print("Couldn't find the definition for " + word)
        return

    for cat, definitions in meaning.items():
        print(cat)
        for definition in definitions:
            print(" " * 5, definition)
        print("")
