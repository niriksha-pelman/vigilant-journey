import tkinter as tk
root = tk.Tk()

root.geometry ("500x500")
root.title("Rock, Paper, Scissors")

label = tk.Label (root, text = "AI vs You" , font= ('Arial',18) )
label.pack()

def start_game():
    new_window = tk.Toplevel()
    new_window.geometry ("500x500")
    tk.Label(page_1=new_window, text="This is a new window").pack()

gamebutton = tk.Button (text="Start Game" , command= start_game)
gamebutton.pack()
root.mainloop()