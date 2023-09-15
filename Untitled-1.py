import tkinter as tk
root = tk.Tk()

root.geometry ("500x500")
root.title("Rock, Paper, Scissors")

label = tk.Label (root, text = "AI vs You" , font= ('Arial',18) )
label.pack()
root.mainloop()