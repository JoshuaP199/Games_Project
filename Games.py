import tkinter
from random import *
import sys



def RPSJP():
#Created by Joshua Perez

    print("Game: Rock, Paper, Scissors vs a Computer\nThe rules are as follow:")

    a = ""
    botlist = ("Rock", "Paper", "Scissors")

    while True:
        
        while True:

            print("\nChoose either rock (r), paper (p), or scissors (s) and see if you beat the bot")
            print("Please use the () letter corresponding to your response.")
            q = input("What will you choose against the bot? ")
            
            if q == "r":
                a = "Rock"
                break
            elif q == "p":
                a = "Paper"
                break
            elif q == "s":
                a = "Scissors"
                break
            else:
                print('You did not enter a valid letter. Restarting...')
                continue

        b = botlist[randint(0,2)]
        print("\nYou chose " + a + " and the bot chose " + b + ".")
        
        if b == "Rock":
            if a == "Rock":
                print("Its a TIE!")
            elif a == "Paper":
                print("You covered the bot. You WIN!")
            elif a == "Scissors":
                print("The bot smashed you. You Lose.")
        elif b == "Paper":
            if a == "Rock":
                print("The bot covered you. You Lose.")
            elif a == "Paper":
                print("Its a TIE!")
            elif a == "Scissors":
                print("You cut the bot. You WIN!")
        elif b == "Scissors":
            if a == "Rock":
                print("You smashed the bot. You WIN!")
            elif a == "Paper":
                print("The bot cut you. You Lose.")
            elif a == "Scissors":
                print("Its a TIE!")

        end = input("\nWould you like to play again? (y) / (n) ")
        if end == "n":
            print('Quitting game.')
            sys.exit()
        elif end == "y":
            continue
        else:
            print('You did not enter a valid letter. Quitting game.')
            sys.exit()

def BackToMenu(): #current issue Doesnt close TTT window so it doesnt allow interface to run
    import gui_tut
    window.destroy()
    #gui_tut.interface()

def TTT():
    #Window Name
    window = tkinter.Tk()
    window.title('Tic Tac Toe')
    window.grid()

    def x(r, c):
        bx = tkinter.Button(text="X", height = 10, width = 20, padx = 5) #when i make these disabled it doesnt work when called from gui_tut
        bx.grid(row= r, column = c)

    def o(r, c):
        bo = tkinter.Button(text="O", height = 10, width = 20, padx = 5)
        bo.grid(row= r, column = c)

    #Buttons
    b1 = tkinter.Button(text="1", height = 10, width = 20, padx = 5) 
    b2 = tkinter.Button(text="2", height = 10, width = 20, padx = 5, command = x(0, 1)) #not working
    b3 = tkinter.Button(text="3", height = 10, width = 20, padx = 5, command = o(0, 2))
    b4 = tkinter.Button(text="4", height = 10, width = 20, padx = 5)
    b5 = tkinter.Button(text="5", height = 10, width = 20, padx = 5)
    b6 = tkinter.Button(text="6", height = 10, width = 20, padx = 5)
    b7 = tkinter.Button(text="7", height = 10, width = 20, padx = 5)
    b8 = tkinter.Button(text="8", height = 10, width = 20, padx = 5)
    b9 = tkinter.Button(text="9", height = 10, width = 20, padx = 5)
    menu = tkinter.Button(text = "Back to Menu", command = BackToMenu, height = 5, width = 18, pady = 10)

    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)
    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)
    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)
    menu.grid(row = 4, column = 1)

    window.mainloop()
