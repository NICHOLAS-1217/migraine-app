from tkinter import *
from tkinter.ttk import *

def login_page():
    
    window = Tk()
    window.geometry('+200+50') 
    window.title("migraine app")

    welcomeLabel = Label(window, text="welcome").grid(row=0, column=1)

    emailLabel = Label(window, text="email").grid(row=1, column=0)
    email = StringVar()
    emailEntry = Entry(window, textvariable=email).grid(row=1, column=1)

    passowrdLabel = Label(window, text="password").grid(row=2, column=0)
    password = StringVar()
    passwordEntry = Entry(window, textvariable=password).grid(row=2, column=1)

    loginButton = Button(window, text="login").grid(row=3, column=1)

    registerButton = Button(window, text='register').grid(row=4, column=2)

    adminLoginButton = Button(window, text='admin').grid(row=4, column=0)

    window.mainloop()
