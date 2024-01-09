import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Widgets.scroll_widgets import *

class DayView(ttk.Frame):

    def __init__(self, master, control, **kargs): # using 'control' as a parameter is a short term fix. REMOVE ASAP!!!
        super().__init__(master, **kargs)
        # declaring the controller as 'self.control'
        self.control = control
        print("This is DayControl!",self.control)
        # create widgets here
        # buttons
        self.registers = []
        self.reg_info = []
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.day_buttons = []
        
        # this iterates through each day Mon-Sun and creates a button.
        for i in range (len(self.days)):
            self.rowconfigure(0, weight=1) # dont need the configs??
            self.columnconfigure(i, weight=1)
            # this section assigns each button a 'name' and a value from 0-6. The button is then created and gridded.
            self.day_buttons.append(ttk.Button(self, text=self.days[i], command= lambda i=i: self.share_day(self.days[i]) )) #  this command will show classes depending on which day was selected.
            self.day_buttons[i].grid(row=0,column=i, sticky="EW", pady=5) # DONT USE PAKCING!!! - matthew :)
        self.reg_widgets("Monday")

    def share_day(self, day):
        self.kill_everything() # this always goes first :))
        self.reg_info(day)
        self.reg_widgets(day)


    def reg_widgets(self, day):
        ## VerticalScrolledFrame uses 'self.reg_frame.interior' 
        self.reg_frame = VerticalScrolledFrame(self)
        self.reg_frame.grid(sticky="NESW")

        self.columnconfigure(0, weight=1)

        num_of_classes = self.control.day_service.get_lessons_day(day) 
        print("Class count",num_of_classes)

        r,c = 1,1
        for count in range (0,len(num_of_classes)):
            # buttons
            self.registers.append(ttk.Button(self.reg_frame.interior, text=f"Register {count+1}")) # will give command soon   
            self.registers[count].grid(row=r, column=0, sticky="EW")
            # class_info
            self.reg_widgets.append(ttk.Label(self.reg_frame.interior, text=f"{}") # need to finish this. Loop through num_of_classes and add relavant data from there into this label.
            self.reg_widgets[count].grid(row=r, column=c, sticky="NESW")
            # when sticky="NESW" it expands the button to be the size of the row. Could use this for the labels to display info on each class within the Register.
            r += 1
            c += 1
        self.registers.clear()

    def kill_everything(self):
        self.reg_frame.destroy()

'''
Lesson --> class_ID --> teacher_ID
                    --> 
'''