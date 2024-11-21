from email.policy import default
from tkinter import *
from tkinter import messagebox as mb

import datetime
import time

window = Tk()
window.title("Напоминалка")
window.geometry("400x300")
window.iconbitmap(default="favicon.ico")

e = Entry(window, font=("Arial"))
e.pack()
btn = Button(window, text="Установить напоминание")
btn.pack()

window.mainloop()