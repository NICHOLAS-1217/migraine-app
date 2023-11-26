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

def login_page():

    from home import home_page
    from register import register_page
    
    loginPanel = tk.Tk()
    style = ttk.Style("superhero")
    loginPanel.geometry('1000x800') 
    loginPanel.title("migraine app")
    loginPanel.resizable(False, False)

    welcomeLabel = ttk.Label(loginPanel, text="welcome").place(x=500, y=250, anchor='center')

    emailLabel = ttk.Label(loginPanel, text="email").place(x=325, y=285)
    email = ttk.StringVar()
    emailEntry = ttk.Entry(loginPanel, textvariable=email).place(x=500, y=300, anchor='center')

    passowrdLabel = ttk.Label(loginPanel, text="password").place(x=325, y=335)
    password = ttk.StringVar()
    passwordEntry = ttk.Entry(loginPanel, textvariable=password).place(x=500, y=350, anchor='center')

    def login_to_home():
        user_email = email.get()
        user_password = password.get()
        if user_email == ""  or user_password == "":
            messagebox.showwarning('WARNING','PLEASE COMPLETE ALL FILLING')
        else: 
            c.execute ('SELECT * FROM user where user_email = %s and user_password = %s', (user_email , user_password))
            if c.fetchone():
                user_login = user_email
                loginPanel.destroy()
                home_page()
            else: 
                messagebox.showwarning('WARNING','PLEASE TRY AGAIN')
            db.commit()
    loginButton = ttk.Button(loginPanel, text="login", command=login_to_home, bootstyle=(LIGHT, OUTLINE)).place(x=500, y=400, anchor='center')

    def login_to_register():
        loginPanel.destroy()
        register_page()
    registerButton = ttk.Button(loginPanel, text='register', command=login_to_register, bootstyle=(LIGHT, OUTLINE)).place(x=963, y=34, anchor="s")

    adminLoginButton = ttk.Button(loginPanel, text='admin', bootstyle=(LIGHT, OUTLINE)).place(x=0, y=0)

    loginPanel.mainloop()


    

