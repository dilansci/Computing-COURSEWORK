import tkinter as tk
from tkinter import ttk
from Controllers.controller import SQLController

'''
The 'View' contains all the UI for the software. It can call methods from the 'controller' class 
through widgets i.e. Buttons. 
** 'View' should never contain any actual code!!! It should only be able to use methods and code
from the controller. **
'''

class DayView(ttk.Frame):

    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        # declaring the controller as 'self.control' and passing the 'view' into controller.py
        self.control = SQLController(DayView)
        # create widgets here
        # buttons
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.day_buttons = []

        # this iterates through each day Mon-Sun and creates a button.
        for i in range (len(self.days)):
            self.rowconfigure(0, weight=1)
            self.columnconfigure(0, weight=1)
            # this section assigns each button a 'name' and a value from 0-6. The button is then created and gridded.
            self.day_buttons.append(ttk.Button(self, text=self.days[i], command= lambda i=i: self.change_day(self.days[i]))) #  this command will show classes depending on which day was selected.
            self.day_buttons[i].grid(row=0,column=i) # DONT USE PAKCING!!! - matthew :)

    def change_day(self, day):
        info = self.control.change_day_reg(day)
        # return(reg_view(info))
        

if __name__ == "__main__":
    dayview = DayView()
    dayview.mainloop()