#Created by Joshua Perez

import tkinter
from tkinter import *
from PIL import ImageTk, Image
import Games

#can make def's of each game and write all the code here in each one or find a way
#to link another file and run it through the def.

def interface(): #change to main menu?
    #Window Name
    window = tkinter.Tk()
    window.title('Games')
    window.geometry("500x700")

    #Image/logo
    path = "square.jpg" #need a png and need to figure out resizing
    img = ImageTk.PhotoImage(Image.open(path))
    panel = tkinter.Label(window, image = img,)
    panel.pack()

    #Beginning Message
    var = StringVar()
    label = Label(window, textvariable = var, pady = 25)
    var.set("Choose a game to play!")
    label.pack()

    #Games
    def rps():
        window.destroy() 
        Games.RPSJP()   
        

    def hm():   #Working but not entirely
        import Hangman
        window.destroy() 
        Hangman.hangman("c")

    
    def gmc(): #NOT WORKING & set the type here in () and transfer it to the one that launched
        import cardGuessingGame
        window.destroy() 
        cardGuessingGame.cardGuessingGame("easy") 

    
    def gmn(): #NOT WORKING
        import guessANumber
        window.destroy() 
        guessANumber.guessANumber("easy")


    def ttt(): #Using Games.py file
        window.destroy()
        Games.TTT()


    #Game Buttons
    GMC = tkinter.Button(text="Guess My Card", bd = 3, width = 20, state = DISABLED)
    HM = tkinter.Button(text ="Hangman", command = hm, bd = 3, width = 20)
    GMN = tkinter.Button(text="Guess My Number", bd = 3, width = 20, state = DISABLED)
    RPS = tkinter.Button(text="Rock Paper Scissors", command = rps, bd = 3, width = 20)
    BS = tkinter.Button(text="BattleShip", bd = 3, width = 20, state = DISABLED)
    TTT = tkinter.Button(text="Tic Tac Toe", bd = 3, width = 20, command = ttt)

    GMC.pack()
    HM.pack()
    GMN.pack()
    RPS.pack()
    BS.pack()
    TTT.pack()
    
    window.mainloop() #Always at bottom of window code

interface()