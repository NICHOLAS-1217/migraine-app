from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from ttkbootstrap.constants import *
import tkinter as tk
import ttkbootstrap as ttk
import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
port='3306',
password="Tanzhixuan_1217",
database="migrainedb"
)
c = db.cursor()

def register_page():

    from login import login_page

    registerPanel = tk.Tk()
    style = ttk.Style("superhero")
    registerPanel.geometry('1000x800') 
    registerPanel.title("migraine app")
    registerPanel.resizable(False, False)

    registerLabel = ttk.Label(registerPanel, text="registration").grid(row=0, column=1)

    nameLabel = ttk.Label(registerPanel, text="username").grid(row=1, column=0)
    name = ttk.StringVar()
    nameEntry = ttk.Entry(registerPanel, textvariable=name).grid(row=1, column=1)

    emailLabel = ttk.Label(registerPanel, text="email").grid(row=2, column=0)
    email = ttk.StringVar()
    emailEntry = ttk.Entry(registerPanel, textvariable=email).grid(row=2, column=1)

    passowrdLabel = ttk.Label(registerPanel, text="password").grid(row=3, column=0)
    password = ttk.StringVar()
    passwordEntry = ttk.Entry(registerPanel, textvariable=password).grid(row=3, column=1)

    def register_success():
        user_name = name.get()
        user_email = email.get()
        user_password = password.get()
        if user_name == ""or user_email == "" or user_password == "":
            messagebox.showwarning('WARNING','PLEASE ENSURE THAT THE INFORMATION ENTERED IS COMPLETE')
        else:
            c.execute('INSERT INTO user VALUES (NULL, %s, %s, %s)', (user_name, user_email, user_password))
            db.commit()
            print(c.rowcount, "record inserted.")
            messagebox.showinfo(title="info", message="success")
            registerPanel.destroy()
            login_page()

    registerButton = ttk.Button(registerPanel, text='register', command=register_success).grid(row=4, column=1)

    def register_to_login():
        registerPanel.destroy()
        login_page()
    backButton = ttk.Button(registerPanel, text='back', command=register_to_login).grid(row=5, column=0)

    caretakerButton = ttk.Button(registerPanel, text='care taker').grid(row=5, column=2)

    registerPanel.mainloop()


