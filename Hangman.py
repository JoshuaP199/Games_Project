def bodyLeft(bodyParts, guessWord):
    if bodyParts == 0:
        print(" ______")
        print("|     |")
        print("|   (- -)")
        print("|   __|__")
        print("|     |  ")
        print("|_   / \\")
    elif bodyParts == 1: 
        print(" ______")
        print("|     |")
        print("|   (- -)")
        print("|   __|")
        print("|     |  ")
        print("|_   / \\")
    elif bodyParts == 2:
        print(" ______")
        print("|     |")
        print("|   (- -)")
        print("|     |")
        print("|     |  ")
        print("|_   / \\")
    elif bodyParts == 3:
        print(" ______")
        print("|     |")
        print("|   (- -)")
        print("|     |")
        print("|     |  ")
        print("|_     \\")
    elif bodyParts == 4:
        print(" ______")
        print("|     |")
        print("|   (- -)")
        print("|     |")
        print("|     |  ")
        print("|_")
    elif bodyParts ==5: 
        print(" ______")
        print("|     |")
        print("|   (- -)")
        print("|")
        print("|_")
    else:
        print("YOU ARE DEAD!!!")
        print("The word was ", guessWord)

def displayWord(guessWord, lettersGuessed):
    r = len(guessWord)
    if len(lettersGuessed) == 0:
        print(r*" _ ")
    else:
        holder = ["_"]*r
        for letter in lettersGuessed:
            letterLocations = []
            i = 0 
            for l in guessWord:
                if letter == l:
                    letterLocations.append(i)
                i+=1
            for ll in letterLocations:
                holder[ll] = letter 
        stringy = ""
        for thingy in holder:
            stringy+= " "
            stringy += thingy
            stringy+= " "
        print(stringy)

def chooseWord():
    import random
    words = ['apple', 'nutmeg', 'pineapple', 'cat', 'pengolin', 'india', 'turkey', 'bicycle', 'python', 'programming', 'netflix', 'wonderland', 'cows', 'vegetarian', 'helpful', 'college',
                'linux', 'horse', 'necklace', 'safe', 'motorboat', 'father', 'relationship', 'murder', 'arsenic', 'vampire', 'twilight', 'wizard', 'socks', 'farmer', 'glass', 'grandparents',
                'flowers', 'rose', 'wine', 'park', 'hummus', 'christmas', 'kangaroo', 'books', 'island', 
                 'woolgthering', 'psithurism', 'fumadiddle', 'novaturient', 'sempiternal', 'gigil', 'imbroglio', 'torpid', 'neologize', 'sarang', 'voorpret', 'hiraeth', 'degust', 'sciolist', 
                 'gegenschien', 'antapology', 'petrichor', 'quixotic', 'anagnorisis', 'alexithymia', 'obviate',
                 'flummox', 'dowdy', 'nincompoop', 'muesli', 'myopic', 'bamboozle', 'phyllo', 'thwart', 'brouhaha', 'zeal', 'pneumatic', 'noxious', 'flimflam', 'abomasum', 'wanderlust']
    return random.choice(words)
def hangman(o):
    if o == 'c':
        guessWord = chooseWord()
    else:
        print("Player 1: Please Enter your word away from Player 2")
        guessWord = input("Enter Word Here: ").lower()
    bodyParts = 0
    guessedLetters = []
    correctLetters = []
    bodyLeft(bodyParts, guessWord)
    displayWord(guessWord, correctLetters)
    guessed = False
    while (bodyParts != 6) or (guessed != True):
        guessedLetters.append(input("Guess a letter").lower())
        if guessedLetters[-1] not in guessWord:
            bodyParts +=1
            bodyLeft(bodyParts, guessWord)
            displayWord(guessWord, correctLetters)
        else: 
            correctLetters.append(guessedLetters[-1])
            displayWord(guessWord, correctLetters)
            bodyLeft(bodyParts, guessWord)
        if len(correctLetters) == len(guessWord):
            guessed = True
