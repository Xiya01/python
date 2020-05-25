import tkinter, time

global button1
global button2
global button3
global button4
global button5
global button6
global button7
global button8
global button9
global clear

window = tkinter.Tk()
tkinter.Label(window, text="Tic-Tac-Toe:").grid(row=0, column=0)
button1 = tkinter.Button(window, text=".")
button2 = tkinter.Button(window, text=".")
button3 = tkinter.Button(window, text=".")
button4 = tkinter.Button(window, text=".")
button5 = tkinter.Button(window, text=".")
button6 = tkinter.Button(window, text=".")
button7 = tkinter.Button(window, text=".")
button8 = tkinter.Button(window, text=".")
button9 = tkinter.Button(window, text=".")
clear = tkinter.Button(window, text= "Clear")

button1.grid(row=2, column=1)
button2.grid(row=2, column=2)
button3.grid(row=2, column=3)
button4.grid(row=3, column=1)
button5.grid(row=3, column=2)
button6.grid(row=3, column=3)
button7.grid(row=4, column=1)
button8.grid(row=4, column=2)
button9.grid(row=4, column=3)
clear.grid(row=6, column=0)

global symbol
symbol = "X"

def check(sign):
    if button1['text'] == sign and button2['text'] == sign and button3['text'] == sign:
        from tkinter import messagebox
        messagebox.showinfo("Result:", sign + " wins !")
        action10()


    elif button4['text'] == sign and button5['text'] == sign and button6['text'] == sign:
        from tkinter import messagebox
        messagebox.showinfo("Result:", sign + " wins !")
        action10()

    elif button7['text'] == sign and button8['text'] == sign and button9['text'] == sign:
        from tkinter import messagebox
        messagebox.showinfo("Result:", sign + " wins !")
        action10()

    elif button1['text'] == sign and button4['text'] == sign and button7['text'] == sign:
        from tkinter import messagebox
        messagebox.showinfo("Result:", sign + " wins !")
        action10()

    elif button2['text'] == sign and button5['text'] == sign and button8['text'] == sign:
        from tkinter import messagebox
        messagebox.showinfo("Result:", sign + " wins !")
        action10()

    elif button3['text'] == sign and button6['text'] == sign and button9['text'] == sign:
        from tkinter import messagebox
        messagebox.showinfo("Result:", sign + " wins !")
        action10()

    elif button1['text'] == sign and button5['text'] == sign and button9['text'] == sign:
        from tkinter import messagebox
        messagebox.showinfo("Result:", sign + " wins !")
        action10()

    elif button3['text'] == sign and button5['text'] == sign and button7['text'] == sign:
        from tkinter import messagebox
        messagebox.showinfo("Result:", sign + " wins !")
        action10()

def action1():
    global symbol
    button1['text'] = symbol
    button1['command'] = ""
    check(symbol)
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"

def action2():
    global symbol
    button2['text'] = symbol   
    button2['command'] = ""
    check(symbol)
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"

def action3():
    global symbol
    button3['text'] = symbol
    button3['command'] = ""
    check(symbol)
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"

def action4():
    global symbol
    button4['text'] = symbol
    button4['command'] = ""
    check(symbol)
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"

def action5():
    global symbol
    button5['text'] = symbol
    button5['command'] = ""
    check(symbol)
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"

def action6():
    global symbol
    button6['text'] = symbol
    button6['command'] = ""
    check(symbol)
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"

def action7():
    global symbol
    button7['text'] = symbol
    button7['command'] = ""
    check(symbol)
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"

def action8():
    global symbol
    button8['text'] = symbol
    button8['command'] = ""
    check(symbol)
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"

def action9():
    global symbol
    button9['text'] = symbol
    button9['command'] = ""
    check(symbol)
    if symbol == "O":
        symbol = "X"
    elif symbol == "X":
        symbol = "O"
    

def action10(): 
    global clear 
    button1['text'] = "."
    button2['text'] = "."
    button3['text'] = "."
    button4['text'] = "."
    button5['text'] = "."
    button6['text'] = "."
    button7['text'] = "."
    button8['text'] = "."
    button9['text'] = "."
    
    global symbol
    symbol = "X"

    button1['command'] = action1
    button2['command'] = action2
    button3['command'] = action3
    button4['command'] = action4
    button5['command'] = action5
    button6['command'] = action6
    button7['command'] = action7
    button8['command'] = action8
    button9['command'] = action9


button1['command'] = action1
button2['command'] = action2
button3['command'] = action3
button4['command'] = action4
button5['command'] = action5
button6['command'] = action6
button7['command'] = action7
button8['command'] = action8
button9['command'] = action9
clear['command'] = action10




window.mainloop()
