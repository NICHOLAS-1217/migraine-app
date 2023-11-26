import tkinter as tk
from  datetime import datetime
from datetime import timedelta
from collections import defaultdict

class Project:
    def __init__(self,parent,controller,project_number):
        # the parent is the "master window" into which the project windows
        # are placed.
        self.controller = controller
        self.parent = parent
        self.project_number = project_number
        self.make_frame()
        
    def make_frame(self):
        con = self.controller
        dex = self.project_number
        
        frame = tk.Frame(master=self.parent, height=100, bg=con.color_palette[dex])
        label = tk.Label(master=frame, text=con.project_list[dex], 
                         justify='left', bg=con.color_palette[dex], fg='white')
        label.place(x=10, y=10, width=60, height=20)
        start_button = tk.Button(frame, text="Start", 
                                 command=lambda : self.start_func(),
                                 bg=con.color_palette[dex])
        start_button.place(x=10, y=45, width=70, height=20)
        stop_button = tk.Button(frame, text="Stop", 
                                command=lambda : self.stop_func(), 
                                bg=con.color_palette[dex])
        stop_button.place(x=90, y=45, width=70, height=20)
        reset_button = tk.Button(frame, text="Reset", 
                                 command=lambda : self.reset_func(), 
                                 bg=con.color_palette[dex])
        reset_button.place(x=170, y=45, width=70, height=20)
        frame.pack(fill=tk.X)
    def start_func(self):
        self.starttime = datetime.now()
        
    def stop_func(self):
        stoptime = datetime.now()
        diff = stoptime - self.starttime
        time_entry = [datetime.today,self.starttime,stoptime,diff]
        self.controller.df[self.project_number].append(time_entry)
        # using a dictionary to hold a list of the start and stop times 

    def reset_func():
        self.controller.df.pop(self.project_num)
            
class display(tk.Tk):
    #This class adds function to the tkinter Tk class
    def __init__(self,project_list):
        self.df = defaultdict(list)
        tk.Tk.__init__(self)   # initialize the window
        self.title("Time Tracking ")
        length = 100+(100*len(project_list))
        self.geometry("250x"+str(length))
        self.frames = []
        self.color_palette = color_palette
        self.project_list = project_list
        for i,fr in enumerate(project_list) :
        self.frames.append(Project(self,  # master of frame
                                       self,  # controller function of frame (happens to be same)
                                       i))
        
if __name__=="__main__" :
    project_list = ['Project 0', 'Project 1']
    color_palette = ['#1e2839','#283347','#434e61','#647187','#c4c5c9']
    root = display(project_list)
    root.mainloop()
                
                