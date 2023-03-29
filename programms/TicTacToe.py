from tkinter import *
import random

def next_turn(row, column):
    global player
    global label
    global end
    if buttons[row][column].cget("text")=="" and end!=True:
        buttons[row][column].config(text=player)
        win = check_winner()
        if win is True:
            label.config(text=player+" won!")
            end = True
        elif win=="Tie":
            label.config(text="Tie!")
        else:
            if(player==players[0]):
                player=players[1]
            else:
                player=players[0]
            label.config(text=player+" turn")

def check_winner():

    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] == player:
            for column in range(3):
                buttons[row][column].config(bg="green")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] == player:
            for row in range(3):
                buttons[row][column].config(bg="green")
            return True

    if buttons[0][0]['text']==buttons[1][1]['text']==buttons[2][2]['text']==player:
        for index in range(3):
            buttons[index][index].config(bg="green")
        return True

    elif buttons[0][2]['text']==buttons[1][1]['text']==buttons[2][0]['text']==player:
        for index in range(3):
            buttons[index][2-index].config(bg="green")
        return True

    elif empty_spaces() is False:
        return "Tie"

    else:
        return False

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column].cget("text")=="":
                return True
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(bg="yellow")
    return False

def new_game():
    global label
    global player
    global end
    player = random.choice(players)
    label.config(text=player+" turn")
    end = False
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="")
            buttons[row][column].config(bg="white")

window = Tk()
window.title("Tic-Tac-Toe")
end = False
players = ["x", "o"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]

label = Label(text=player + " turn", font=("consolas", 40))
label.pack(side="top")

reset_button = Button(text="restart", font=('consolas', 20), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text="", width=5, height=2, font=('consolas', 40),
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

window.mainloop()