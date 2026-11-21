from tkinter import *
from tkinter import messagebox
import random

p = 0
t = 15
def click():
    global p
    p += 1
    score["text"] = "POINTS: " + str(p)
    apple.place(x=random.randint(50, 500), y=random.randint(50, 400))

def move():
    if t > 0:
        apple.place(x=random.randint(50, 500), y=random.randint(50, 400))
        window.after(700, move)
def timer():
    global t
    if t > 0:
        t -= 1
        time["text"] = "TIME: " + str(t)
        window.after(1000, timer)
    else:
        apple.place_forget()
        messagebox.showinfo("GAME OVER", "POINTS: " + str(p))
def start():
    start_btn.place_forget()
    time.place(x=20, y=20)
    score.place(x=450, y=20)

    apple.config(bg="turquoise", activebackground="turquoise")

    apple.place(x=250, y=200)
    timer()
    move()

window = Tk()
window.geometry("600x500")
window.config(bg="turquoise")

img = PhotoImage(file="apple.png").subsample(8, 8)
time = Label(window, text="TIME: 15", bg="turquoise")
score = Label(window, text="POINTS: 0", bg="turquoise")

start_btn = Button(window, text="START GAME", command=start)
start_btn.place(x=230, y=220)
apple = Button(
    window,
    image=img,
    border=0,
    bg="turquoise",
    activebackground="turquoise",
    command=click
)

window.mainloop()
