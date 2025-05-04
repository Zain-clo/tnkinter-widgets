import tkinter as tk
import random

def p(c):
    m = ['Rock', 'Paper', 'Scissors']
    comp = random.choice(m)
    r = "Tie!"
    if (c, comp) in [('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')]: r = "Win!"
    elif c != comp: r = "Lose!"
    l.config(text=f"You: {c}\nComp: {comp}\n{r}")

root = tk.Tk()
l = tk.Label(root)
l.pack()

tk.Button(root, text="Rock", command=lambda: p("Rock")).pack()
tk.Button(root, text="Paper", command=lambda: p("Paper")).pack()
tk.Button(root, text="Scissors", command=lambda: p("Scissors")).pack()

root.mainloop()