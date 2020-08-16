#def highLow(): 
    

def guess(answer):
    g = input("Guess a number: ")
    guessCheck(answer, g)
    
def guessCheck(answer, guess):
    if guess == answer:
        print("You have won")
    else:
        if input('Do you want to guess again (y): ') == 'y':
            guess(answer)
        else: 
            menu()
        

def guessANumber(level):
    f = input("Do you want to choose the range: (y) or (n)")
    if f.lower() == 'y':
        ub = input("What do you want to be the upperboundary of the range to be: ")
        luckyNum = random.randint(0, ub)
    else:
        luckyNum = random.randint(0, 100)
    if level == 'easy':
        #hot and cold
    else:
        guess(luckyNum)
        
    
