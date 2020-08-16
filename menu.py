def chooseGame(gc):
    #Guess My Card
    if gc == "1":
        level = input("Would you like to play easy or hard?")
        if (level != 'easy') or (level != 'hard'):
            print("Incorrect input choice\nPlease only enter either: easy or hard")
            chooseGame(gc)
        cardGuessingGood(level)
    #Hangman
    elif gc == "2":
        opponent = input("Do you want to play against a computer (c) or human (h)")
        if (opponent.lower() != 'c') or (opponent.lower() != 'h'):
            print("Incorrect input, please enter either 'c' for computer or 'h' for human")
            chooseGame(gc)
        '''
        level = input("Would you like to play easy or hard?")
        if (level != 'easy') or (level != 'hard'):
            print("Incorrect input choice\nPlease only enter either: easy or hard")
            chooseGame(gc)'''
        hangman(opponent)
    
    #Guess a number
    elif gc == "3":
        level = input("Would you like to play easy or hard?")
        if (level != 'easy') or (level != 'hard'):
            print("Incorrect input choice\nPlease only enter either: easy or hard")
            chooseGame(gc)
        guessANumber(level)
    
    #Rock Paper Scissors
    elif gc == "4":
        opponent = input("Do you want to play against a computer (c) or human (h)")
        if (opponent.lower() != 'c') or (opponent.lower() != 'h'):
            print("Incorrect input, please enter either 'c' for computer or 'h' for human")
            chooseGame(gc)
        rps(opponent)
        
    #Battleship
    elif gc == "5":
        
    #tic tac toe
    elif gc == "6":
        
    

def menu():
    print("1. Guess my Card\n2. Hangman\n3. Guess a number\n4. Rock Paper Scissors\n5. BattleShip\n6. tac tac toe\n")
    gameChoice = input('What game would you like to play (select number)\n')
    if gameChoice not in range(1,7):
        print("That is an invalid Selection, please choose again\n")
        menu()
    chooseGame(gameChoice)
        
