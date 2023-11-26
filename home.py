from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkcalendar import Calendar
import tkinter as tk
import datetime
import mysql.connector

db = mysql.connector.connect(
host="localhost",
user="root",
port='3306',
password="Tanzhixuan_1217",
database="migrainedb"
)
c = db.cursor()

current_time = datetime.datetime.now()

def home_page():

    homePanel = tk.Tk()
    homePanel.geometry('+200+50') 
    homePanel.title("migraine app")

    cal = Calendar(homePanel, selectmode='day',year=current_time.year, month=current_time.month, day=current_time.day)
    cal.pack(pady = 20)
    def date():
        date.config(text = "Selected Date is: " + cal.get_date())
    Button(homePanel, text = "Get Date",command = date).pack(pady = 20)
    date = Label(homePanel, text = "")
    date.pack(pady = 20)
   
    # Pain Level
    pain_label = tk.Label(homePanel, text="Pain Level (1-10):")
    pain_label.pack()
    pain_scale = tk.Scale(homePanel, from_=1, to=10, orient=tk.HORIZONTAL)
    pain_scale.pack()

    # Triggers
    triggers_label = tk.Label(homePanel, text="Triggers:")
    triggers_label.pack()
    triggers_entry = tk.Entry(homePanel)
    triggers_entry.pack()

    # Symptoms
    symptoms_label = tk.Label(homePanel, text="Symptoms:")
    symptoms_label.pack()
    symptoms_entry = tk.Entry(homePanel)
    symptoms_entry.pack()

    # Medications
    medications_label = tk.Label(homePanel, text="Medications:")
    medications_label.pack()
    medications_entry = tk.Entry(homePanel)
    medications_entry.pack()

    # Activities
    activities_label = tk.Label(homePanel, text="Activities:")
    activities_label.pack()
    activities_entry = tk.Entry(homePanel)
    activities_entry.pack()

    # Sleep Quality
    sleep_quality_label = tk.Label(homePanel, text="Sleep Quality:")
    sleep_quality_label.pack()
    sleep_quality_var = tk.StringVar()
    sleep_quality_entry = tk.Entry(homePanel, textvariable=sleep_quality_var)
    sleep_quality_entry.pack()

    # Weather
    weather_label = tk.Label(homePanel, text="Weather:")
    weather_label.pack()
    weather_entry = tk.Entry(homePanel)
    weather_entry.pack()

    # Hydration
    hydration_label = tk.Label(homePanel, text="Hydration:")
    hydration_label.pack()
    hydration_var = tk.StringVar()
    hydration_entry = tk.Entry(homePanel, textvariable=hydration_var)
    hydration_entry.pack()

    # Stress Level
    stress_label = tk.Label(homePanel, text="Stress Level (1-10):")
    stress_label.pack()
    stress_scale = tk.Scale(homePanel, from_=1, to=10, orient=tk.HORIZONTAL)
    stress_scale.pack()

    # Productivity
    productivity_label = tk.Label(homePanel, text="Productivity Impact:")
    productivity_label.pack()
    productivity_entry = tk.Entry(homePanel)
    productivity_entry.pack()

    # Save Button
    def save_data():
        pain_level = pain_scale.get()
        triggers = triggers_entry.get()
        symptoms = symptoms_entry.get()
        medications = medications_entry.get()
        activities = activities_entry.get()
        sleep_quality = sleep_quality_var.get()
        weather = weather_entry.get()
        hydration = hydration_var.get()
        stress_level = stress_scale.get()
        productivity = productivity_entry.get()

        # Save this data to a file or database
        # You can customize this part to suit your storage needs

        # Show confirmation message
        messagebox.showinfo("Saved", "Data saved successfully!")
    save_button = tk.Button(homePanel, text="Save", command=save_data)
    save_button.pack()

    # Run the application
    homePanel.mainloop()