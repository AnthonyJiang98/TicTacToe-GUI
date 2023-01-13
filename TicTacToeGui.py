from tkinter import *
from tkinter import messagebox

def Turn(i, j):
    global player
    global x
    global y

    if buttons[i][j]["text"] == "" and Winner() == False:

        if player == players[0]:
            buttons[i][j]["text"] = player
            if Winner() == False:
                player = players[1]
                label.config(text = (player + " turn"))
            elif Winner() == True:
                x+=1
                label.config(text= (players[0] + " wins"))
                score_label.config(text= players[0] + " Score: " + str(x) + " | " + players[1] + " Score: " + str(y))
            elif Winner() == "Tie":
                label.config(text=("tie"))
        else:
            buttons[i][j]["text"] = player
            if Winner() == False:
                player = players[0]
                label.config(text = (player + " turn"))
            elif Winner() == True:
                y+=1
                label.config(text= (players[1] + " wins"))
                score_label.config(text= players[0] + " Score: " + str(x) + " | " + players[1] + " Score: " + str(y))
            elif Winner() == "Tie":
                label.config(text=("tie"))

def Winner():

    #check row win
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            buttons[i][0].config(bg= "green")
            buttons[i][1].config(bg= "green")
            buttons[i][2].config(bg= "green")
            return True
    #check j win
    for j in range(3):
        if buttons[0][j]["text"] == buttons[1][j]["text"] == buttons[2][j]["text"] != "":
            buttons[0][j].config(bg= "green")
            buttons[1][j].config(bg= "green")
            buttons[2][j].config(bg= "green")

            return True
    #check diagonal win
    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
            buttons[0][0].config(bg= "green")
            buttons[1][1].config(bg= "green")
            buttons[2][2].config(bg= "green")
            return True
    elif buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
            buttons[0][2].config(bg= "green")
            buttons[1][1].config(bg= "green")
            buttons[2][0].config(bg= "green")
            return True
    elif Empty() == False:
        for i in range(len(buttons)):
            for j in range(len(buttons[0])):
                buttons[i][j].config(bg= "light blue")
        return "Tie"
    else:
        return False

def Empty():
    spaces = 0
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] != "":
                spaces +=1
    if spaces == 9:
        return False
    else:
        return True

def NewGame():
    global player

    player = players[0]
    label.config(text = player+ " turn")

    for i in range(len(buttons)):
        for j in range(len(buttons[0])):
            buttons[i][j].config(text="", bg="#F0F0F0")

root = Tk()
root.title("TicTacToe")

players = ["O", "X"]
player = players[0]
buttons = [[0,1,2],
           [3,4,5],
           [6,7,8]]

label = Label(text= player + " turn", font =("Ariel", 40))
label.pack(side= "top")

x=0
y=0
score_label = Label(text = players[0] + " Score: 0 | " + players[1] + " Score: 0", font = ("Ariel", 40))
score_label.pack(side = "top")
reset = Button(text = "Restart?", font = ("Ariel", 20), command = NewGame)
reset.pack(side = "bottom")

frame = Frame(root)
frame.pack()

for i in range(len(buttons)):
    for j in range(len(buttons[0])):
        buttons[i][j] = Button(frame, text= "", font=("Ariel", 40),  width= 5, height= 2,
        command=lambda row = i,column = j: Turn(row,column))
        buttons[i][j].grid(row=i,column=j)


root.mainloop()


