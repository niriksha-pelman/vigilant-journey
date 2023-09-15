from  tkinter import *
import random
root = Tk()

root.geometry ("500x500")
root.title("Rock, Paper, Scissors")

label = Label (root, text = "AI vs You" , font= ('Arial',18) )
label.pack()

def start_game():
    def rock():
        rand = random.randint(0,2)
        ai_choice= game_play[rand]
        Label(new_window, text="The AI choose" +" " + ai_choice).pack()
        if ai_choice == "rock":
            Label(new_window, text="Tied").pack()
        elif ai_choice == "scissors":
            Label(new_window, text="You Win!").pack()
            user_win +=1
        else:
            Label(new_window, text="You Lose :(").pack()
            ai_win +=1
        
    def paper():
        rand = random.randint(0,2)
        ai_choice= game_play[rand]
        Label(new_window, text="The AI chooses" + "" + ai_choice).pack()
        if ai_choice == "paper":
            Label(new_window, text="Tied").pack()
        elif ai_choice == "rock":
            Label(new_window, text="You Win!").pack()
            user_win +=1
        else:
            Label(new_window, text="You Lose :(").pack()
            ai_win +=1
        
    def scissors():
        rand = random.randint(0,2)
        ai_choice= game_play[rand]
        Label(new_window, text="The AI choose" + " " +ai_choice).pack()
        if ai_choice == "scissors":
            Label(new_window, text="Tied").pack()
        elif ai_choice == "paper":
            Label(new_window, text="You Win!").pack()
            user_win +=1
        else:
            Label(new_window, text="You Lose :(").pack()
            ai_win +=1

    new_window = Toplevel()
    new_window.title("Game Play")
    new_window.geometry ("500x500")
    ai_win = 0
    user_win =0
    game_play = ["rock","paper","scissors"]
    Label(new_window, text="Pick rock, paper or scissors").pack()
    rockbutton = Button (new_window,text="Rock", command = rock)
    rockbutton.pack()
    paperbutton = Button (new_window,text="Paper",command = paper)
    paperbutton.pack()
    scissorbutton = Button (new_window,text="Scissors", command = scissors)
    scissorbutton.pack()
    quitbutton = Button (new_window,text="Quit")
    quitbutton.pack()
        # if quitbutton:
        #     break
        # rand = random.randint(0,2)
        # ai_choice= game_play[rand]
        # Label(new_window, text="The AI choose" + ai_choice).pack()
        # if rockbutton == ai_choice:
        #     Label(new_window, text="Tied").pack()
        # elif rockbutton and ai_choice == "scissors":
        #     Label(new_window, text="You Win!").pack()
        #     user_win +=1
        # elif paperbutton and ai_choice == "rock":
        #     Label(new_window, text="You Win!").pack()
        #     user_win +=1
        # elif scissorbutton and ai_choice == "paper":
        #     Label(new_window, text="You Win!").pack()
        #     user_win +=1
        # else:
        #     Label(new_window, text="You Lose :()").pack()
        #     ai_win +=1
    

    

    




    



gamebutton = Button (root, text="Start Game" , command= start_game)
gamebutton.pack()
mainloop()