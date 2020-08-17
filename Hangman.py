###############################
#  Created by Gillian Covillo #
#         @gcovillo           #
###############################

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
        return stringy

def chooseWord():
    import random
    words = ['apple', 'nutmeg', 'pineapple', 'cat', 'pengolin', 'india', 'turkey', 'bicycle', 'python', 'programming', 'netflix', 'wonderland', 'cows', 'vegetarian', 'helpful', 'college',
                'linux', 'horse', 'necklace', 'safe', 'motorboat', 'father', 'relationship', 'murder', 'arsenic', 'vampire', 'twilight', 'wizard', 'socks', 'farmer', 'glass', 'grandparents',
                'flowers', 'rose', 'wine', 'park', 'hummus', 'christmas', 'kangaroo', 'books', 'island', 
                 'woolgthering', 'psithurism', 'fumadiddle', 'novaturient', 'sempiternal', 'gigil', 'imbroglio', 'torpid', 'neologize', 'sarang', 'voorpret', 'hiraeth', 'degust', 'sciolist', 
                 'gegenschien', 'antapology', 'petrichor', 'quixotic', 'anagnorisis', 'alexithymia', 'obviate',
                 'flummox', 'dowdy', 'nincompoop', 'muesli', 'myopic', 'bamboozle', 'phyllo', 'thwart', 'brouhaha', 'zeal', 'pneumatic', 'noxious', 'flimflam', 'abomasum', 'wanderlust']
    return random.choice(words)


#########################
#  Geeks for Geeks      #
#########################
def removeChar(s, c) :  #
    counts = s.count(c) #
    s = list(s)         #
    while counts :      #
        s.remove(c)     #
        counts -= 1     #
    s = '' . join(s)    #
    return s            #
#########################
#  Geeks for Geeks      #
#########################


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
    while True:
        print("Guessed Letters: ", [letter for letter in guessedLetters])
        alphabet = ["a", 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                    'v', 'w', 'y', 'x', 'z']
        gl = input("Guess a letter: ")
        if gl not in alphabet:
            print("Please enter only one letter!")
            continue
        if gl in guessedLetters:
            print("You have already guessed this letter, please guess again!")
            continue
        guessedLetters.append(gl)
        if gl not in guessWord:
            bodyParts +=1
            bodyLeft(bodyParts, guessWord)
            word = str(displayWord(guessWord, correctLetters))
            print(word)
        else: 
            correctLetters.append(gl)
            word = str(displayWord(guessWord, correctLetters))
            bodyLeft(bodyParts, guessWord)
            print(word)
                       
        word = removeChar(word, " ")
        word = removeChar(word, "_")
        if len(word) == len(guessWord):
            print("You Won!")
            if (input("Do you want to play again?") == 'y'):
                hangman('c')
            else:
                menu()      
        elif (bodyParts == 6):
            print("YOU ARE DOOMED TO ETERNAL DAMNATION!")
            if (input("Do you want to play again?") == 'y'):
                hangman('c')
            else:
                menu()
           
