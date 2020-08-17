#Created by Joshua Perez

import tkinter
from tkinter import *

def TTT():
    #Window Name
    window = tkinter.Tk()
    window.title('Tic Tac Toe')
    window.grid()

    def x(r, c):
        bx = tkinter.Button(text="X", height = 10, width = 20, padx = 5, state = DISABLED)
        bx.grid(row= r, column = c)

    def o(r, c):
        bo = tkinter.Button(text="O", height = 10, width = 20, padx = 5, state = DISABLED)
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

    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 2)
    b4.grid(row = 1, column = 0)
    b5.grid(row = 1, column = 1)
    b6.grid(row = 1, column = 2)
    b7.grid(row = 2, column = 0)
    b8.grid(row = 2, column = 1)
    b9.grid(row = 2, column = 2)

    window.mainloop()

#TTT()