from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import *
import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
port='3306',
password="Tanzhixuan_1217",
database="migrainedb"
)
c = db.cursor()

from main import login_page

def register_page():

    registerPanel = Tk()
    registerPanel.geometry('+200+50') 
    registerPanel.title("migraine app")

    welcomeLabel = Label(registerPanel, text="registration").grid(row=0, column=1)

    nameLabel = Label(registerPanel, text="username").grid(row=1, column=0)
    name = StringVar()
    nameEntry = ttk.Entry(registerPanel, textvariable=name).grid(row=1, column=1)

    emailLabel = Label(registerPanel, text="email").grid(row=2, column=0)
    email = StringVar()
    emailEntry = ttk.Entry(registerPanel, textvariable=email).grid(row=2, column=1)

    passowrdLabel = Label(registerPanel, text="password").grid(row=3, column=0)
    password = StringVar()
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
    backButton = Button(registerPanel, text='back', command=register_to_login).grid(row=5, column=0)

    caretakerButton = Button(registerPanel, text='care taker').grid(row=5, column=2)

    registerPanel.mainloop()
