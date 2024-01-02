import tkinter as tk
from tkinter import ttk
import sqlite3
from Controllers.controller import RegController


class RegisterView(ttk.Frame):

    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self.control = RegController(RegisterView)

        # make a SQL query here which gets the number of classes and generates a button for each
        self.cursor.execute('''SELECT COUNT(class_ID) as classCount FROM Class''')
        classCount = self.cursor.fetchall()
        for count in classCount:
            r, c = 1, 0
            self.reg_button = tk.Button(self, text=f"Register(classCount)").grid(row=r, column=c)


        # create labels for each class to store the registers.

        ## currently trying to make a view to put reg_model into. Maybe a stack of labels??