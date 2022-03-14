from tkinter import *
import random
 

r = Tk()
r.geometry("300x300")
r.title("Rock Paper Scissor Game")
 
# Value that selectable by comp.
computer_value = {
    "0":"Rock",
    "1":"Paper",
    "2":"Scissor"
}
 
# Need reset to status
def reset_game():
    b1["state"] = "active"  # initialized as active to choose by player.
    b2["state"] = "active"
    b3["state"] = "active"
    l1.config(text = "Player              ")
    l3.config(text = "Computer")
    l4.config(text = "")
 
# Disable the Button
def button_disable():
    b1["state"] = "disable" # after player select any on section, all items will be disabled.
    b2["state"] = "disable"
    b3["state"] = "disable"
 
# we have to define 3 selection in own algortihm that includes rock,paper N scissor.

#first one is if player selected 'rock'
def rock():
    compSlc = computer_value[str(random.randint(0,2))] #select random item in 'computer_value' list.
    if compSlc == "Rock":
        result = "Draw"
    elif compSlc=="Scissor":
        result = "User Win"
    else:
        result = "Comp Win"
    l4.config(text = result)
    l1.config(text = "Rock            ")
    l3.config(text = compSlc)
    button_disable()
 
# If player selected paper
def paper():
    compSlc = computer_value[str(random.randint(0, 2))]
    if compSlc == "Paper":
        result = "Draw"
    elif compSlc=="Scissor":
        result = "Comp Win"
    else:
        result = "User Win"
    l4.config(text = result)
    l1.config(text = "Paper           ")
    l3.config(text = compSlc)
    button_disable()
 
# If player selected scissor
def scissor():
    compSlc = computer_value[str(random.randint(0,2))]
    if compSlc == "Rock":
        result = "Comp. Win"
    elif compSlc == "Scissor":
        result = "Draw"
    else:
        result = "User Win"
    l4.config(text = result)
    l1.config(text = "Scissor         ")
    l3.config(text = compSlc)
    button_disable()
 
# Using buttons frames and labels to functionalities.
Label(r,
      text = "Rock Paper Scissor",
      font = "normal 15 bold",
      fg = "purple").pack(pady = 30)
 
frame = Frame(r) #using frame forgrouping and organizing other widgets in a somehow friendly way.
frame.pack()
 
l1 = Label(frame,
           text = "Player              ",
           font = 10)
 
l2 = Label(frame,
           text = "VS             ",
           font = "normal 10 bold")
 
l3 = Label(frame, text = "Computer", font = 10)
 
l1.pack(side = LEFT)
l2.pack(side = LEFT)
l3.pack(side = LEFT)
 
l4 = Label(r,
           text = "",
           font = "normal 20 bold",
           bg = "white",
           width = 15 ,
           borderwidth = 2,
           relief = "solid")
l4.pack(pady = 20)
 
frame1 = Frame(r)
frame1.pack()
 
b1 = Button(frame1, text = "Rock",
            font = 10, width = 7,
            command = rock) # with 'command' param, using funct of 'rock' means user selected item is rock
 
b2 = Button(frame1, text = "Paper ",
            font = 10, width = 7,
            command = paper) # user selected item is paper
 
b3 = Button(frame1, text = "Scissor",
            font = 10, width = 7,
            command = scissor) # user selected item is scissor
 
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT,padx = 10)
b3.pack(padx = 10)
 
Button(r, text = "Reset",
       font = 10, fg = "red",
       bg = "gray", command = reset_game).pack(pady = 20)
 
r.mainloop()