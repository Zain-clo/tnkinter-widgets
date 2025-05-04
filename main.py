from tkinter import *
from PIL import Image , ImageTk
from tkinter import messagebox

window= Tk()
window.geometry("400x400")



uploaded= Image.open("LOCKSCREEN.png")

bot = ImageTk.PhotoImage(uploaded)

#ibl1 = Label(window , image= bot, width=400 , height=400)
#ibl1.pack()
def msg():
    messagebox.showerror("Error!", "An error occured")
    messagebox.showinfo("Information", "You have just won 1000 dollaes")
    messagebox.showwarning("Alert!", "Virus detected")
    messagebox.askquestion("QUESTION!", "Do you like pizza")
    messagebox.askyesnocancel("Qsn","Do you like coding")
    messagebox.askretrycancel("QSN!", "loading error")


btn = Button(window, text="click here!" , bg="red", command=msg)
btn.pack()


window.mainloop()

