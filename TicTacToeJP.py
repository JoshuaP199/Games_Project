#Created by Joshua Perez

import tkinter as tk
from tkinter import *

player = 0
counter = 0

#NEED TO MAKE IT SO THAT THE WINNER IS DISPLAYED IN A POP UP, NOT IN THE TERMINAL AND HAVE A PLAY AGAIN/BACK TO MENU BUTTON

def TTT():
    #Window Name
    window = Tk()
    window.title('Tic Tac Toe')

    #Window bar with settings like how VS code has file edit ect. at the top
    '''
    frame = Frame(window)
    frame.grid()

    menuBar = Menu(frame)
    menuBar.add_command(label = "Restart", command = Tk.update) #want to make a restart button
    window.config(menu = menuBar)
    '''
    
    #Disables all buttons once game is over
    def bDisable():
        b1.configure(state = DISABLED)
        b2.configure(state = DISABLED)
        b3.configure(state = DISABLED)
        b4.configure(state = DISABLED)
        b5.configure(state = DISABLED)
        b6.configure(state = DISABLED)
        b7.configure(state = DISABLED)
        b8.configure(state = DISABLED)
        b9.configure(state = DISABLED)

    #places X and O on selected spots
    def marker(b):
        global player 
        global counter

        if b["text"] == "" and player == 0: #checks if "text" within the button is blank and sees which player is choosing
            b["text"] = "X"
            player += 1
            counter += 1
        elif b["text"] == "" and player == 1:
            b["text"] = "O"
            player -= 1
            counter += 1

        check(b1,b2,b3,b4,b5,b6,b7,b8,b9, b["text"])

        if counter == 9:
            print("Game Over")
            bDisable()

#Check is very slow at displaying
    def check(b1,b2,b3,b4,b5,b6,b7,b8,b9, m): #checks for win conditions 
        #print(m)
        #print(b1["text"] == b2["text"] == b3["text"] == "X")
        if (b1["text"] == b2["text"] == b3["text"] == "X") or (b1["text"] == b2["text"] == b3["text"] == "O"):
            print(m, "Wins!")
            bDisable()
        elif (b1["text"] == b4["text"] == b7["text"] == "X") or (b1["text"] == b4["text"] == b7["text"] == "O"):
            print(m, "Wins!")
            bDisable()
        elif (b1["text"] == b5["text"] == b9["text"] == "X") or (b1["text"] == b5["text"] == b9["text"] == "O"):
            print(m, "Wins!")
            bDisable()
        elif (b3["text"] == b6["text"] == b9["text"] == "X") or (b3["text"] == b6["text"] == b9["text"] == "O"):
            print(m, "Wins!")
            bDisable()
        elif (b7["text"] == b8["text"] == b9["text"] == "X") or (b7["text"] == b8["text"] == b9["text"] == "O"):
            print(m, "Wins!")
            bDisable()
        elif (b7["text"] == b5["text"] == b3["text"] == "X") or (b7["text"] == b5["text"] == b3["text"] == "O"):
            print(m, "Wins!")
            bDisable()
        elif (b2["text"] == b5["text"] == b8["text"] == "X") or (b2["text"] == b5["text"] == b8["text"] == "O"):
            print(m, "Wins!")
            bDisable()
        elif (b4["text"] == b5["text"] == b6["text"] == "X") or (b4["text"] == b5["text"] == b6["text"] == "O"):
            print(m, "Wins!")
            bDisable()
        

    #Buttons
    b1 = tk.Button(text="", height = 10, width = 20, padx = 5, command = lambda: marker(b1))
    b2 = tk.Button(text="", height = 10, width = 20, padx = 5, command = lambda: marker(b2))
    b3 = tk.Button(text="", height = 10, width = 20, padx = 5, command = lambda: marker(b3))
    b4 = tk.Button(text="", height = 10, width = 20, padx = 5, command = lambda: marker(b4))
    b5 = tk.Button(text="", height = 10, width = 20, padx = 5, command = lambda: marker(b5))
    b6 = tk.Button(text="", height = 10, width = 20, padx = 5, command = lambda: marker(b6))
    b7 = tk.Button(text="", height = 10, width = 20, padx = 5, command = lambda: marker(b7))
    b8 = tk.Button(text="", height = 10, width = 20, padx = 5, command = lambda: marker(b8))
    b9 = tk.Button(text="", height = 10, width = 20, padx = 5, command = lambda: marker(b9))
    #menu = tkinter.Button(text = "Back to Menu", command = BackToMenu, height = 5, width = 18, pady = 10)

    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)
    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)
    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)
    #menu.grid(row = 3, column = 1)

    window.mainloop()

TTT()
