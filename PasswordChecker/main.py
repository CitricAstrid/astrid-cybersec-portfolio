import string
import re
from getpass import getpass
import tkinter as tk
from tkinter import ttk

window = tk.Tk()

label = tk.Label(text="Enter your password: ")
label.pack()
window.geometry("200x100")
window.title("Password Strength Checker")

password_entry = ttk.Entry(window, show="*")
password_entry.pack(pady=5)
password_entry.focus()

def check_password():
    if (len(password_entry.get()) >= 10 and len(password_entry.get()) <= 20
        and re.search("[a-z]", password_entry.get())
        and re.search("[A-Z]", password_entry.get())
        and re.search("[0-9]", password_entry.get())
        and re.search("[_@$£!,&*]", password_entry.get())):
        label.config(text= "This password is strong.")
    else:
        label.config(text="This password is weak.")


button = ttk.Button(window, text="Check Password", command=lambda: check_password())
button.pack(pady=5)

window.mainloop()