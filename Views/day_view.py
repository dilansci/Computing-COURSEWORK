import tkinter as tk
from tkinter import ttk
# from SQL_controller import *

class DayView(ttk.Frame):

    def __init__(self, master, control, **kargs): # using 'control' as a parameter is a short term fix. REMOVE ASAP!!!
        super().__init__(master, **kargs)
        # declaring the controller as 'self.control'
        self.control = control
        print("This is DayControl!",self.control)
        # create widgets here
        # buttons
        self.registers = []
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.day_buttons = []
        
        # this iterates through each day Mon-Sun and creates a button.
        for i in range (len(self.days)):
            self.rowconfigure(0, weight=1) # dont need the configs??
            self.columnconfigure(i, weight=1)
            # this section assigns each button a 'name' and a value from 0-6. The button is then created and gridded.
            self.day_buttons.append(ttk.Button(self, text=self.days[i], command= lambda i=i: self.share_day(self.days[i]) )) #  this command will show classes depending on which day was selected.
            self.day_buttons[i].grid(row=0,column=i, sticky="EW", pady=5) # DONT USE PAKCING!!! - matthew :)
        self.reg_buttons("Monday")

    def share_day(self, day):
        self.change_day(day)
        self.reg_buttons(day)
        

    def reg_buttons(self, day):
            
        # KINDA WANT TO MAKE A FRAME NGL. Would be easier to just clear the whole frame than specifically target each fo the reg_buttons ://.
        self.columnconfigure(0, weight=1)

        classCount = len(self.control.day_service.get_lessons_day(day))
        print("Class count",classCount)
        r = 1
        for count in range (0,classCount):
            self.registers.append(ttk.Button(self, text=f"Register({count+1})")) # will give command soon
            self.registers[count].grid(row=r, column=0, sticky="EW")
            # when sticky="NESW" it expands the button to be the size of the row. Could use this for the labels to display info on each class within the Register.
            r += 1

    def change_day(self, day):
        # this function is kinda pointless ://. Might incorporate it into 'reg_buttons'
        day_change = self.control.day_service.get_lessons_day(day) # Is this a proper solution?? I feel like i am hardcoding the path??
        print(day_change)
        
