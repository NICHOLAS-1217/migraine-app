from tkinter import *
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

def login_page():

    from register import register_page
    
    loginPanel = Tk()
    loginPanel.geometry('+200+50') 
    loginPanel.title("migraine app")

    welcomeLabel = Label(loginPanel, text="welcome").grid(row=0, column=1)

    emailLabel = Label(loginPanel, text="email").grid(row=1, column=0)
    email = StringVar()
    emailEntry = Entry(loginPanel, textvariable=email).grid(row=1, column=1)

    passowrdLabel = Label(loginPanel, text="password").grid(row=2, column=0)
    password = StringVar()
    passwordEntry = Entry(loginPanel, textvariable=password).grid(row=2, column=1)

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
                print("hiahia")
            else: 
                messagebox.showwarning('WARNING','PLEASE TRY AGAIN')
            db.commit()
    loginButton = Button(loginPanel, text="login", command=login_to_home).grid(row=3, column=1)

    def login_to_register():
        loginPanel.destroy()
        register_page()
    registerButton = Button(loginPanel, text='register', command=login_to_register).grid(row=4, column=2)

    adminLoginButton = Button(loginPanel, text='admin').grid(row=4, column=0)

    loginPanel.mainloop()
