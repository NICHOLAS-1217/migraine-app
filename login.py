from tkinter import *
from tkinter.ttk import *


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

    loginButton = Button(loginPanel, text="login").grid(row=3, column=1)

    def login_to_register():
        loginPanel.destroy()
        register_page()
    registerButton = Button(loginPanel, text='register', command=login_to_register).grid(row=4, column=2)

    adminLoginButton = Button(loginPanel, text='admin').grid(row=4, column=0)

    loginPanel.mainloop()
