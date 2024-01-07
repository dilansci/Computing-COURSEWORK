import tkinter as tk
from tkinter import ttk
# from Controllers.reg_controller import RegController

class RegisterView(ttk.Frame):

    def __init__(self, master, day, control, **kargs):
        super().__init__(master, **kargs)
        self.control = control
        print("This is RegControl!",self.control)
        # make a SQL query here which gets the number of classes and generate a button for each

        # creat widgets here
        self.reg_container = tk.Frame(self,highlightcolor="blue", highlightthickness=5, highlightbackground="blue")
        self.reg_container.columnconfigure(0, weight=1) 
        self.reg_container.rowconfigure(0, weight=1)
        self.reg_container.grid(sticky="E")

        classCount = len(self.control.reg_factory(day))
        print("Class count",classCount)
        r, c = 1, 0
        for count in range (0,classCount):
            self.reg_button = ttk.Button(self.reg_container, text=f"Register({count+1})")
            self.reg_button.grid(row=r, column=c,sticky="W")
            r += 1


        # create labels for each class to store the registers.

        ## currently trying to make a view to put reg_model into. Maybe a stack of labels??