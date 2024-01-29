import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager

class Exit(tk.LabelFrame):
    '''
    This class will be constantly tracking what the previous View was. 
    I'm thinking of making a dictionary which stores all views once they are accessed (Login being the very first view) 
    and when 'Exit' is called, then it goes to the previous view and deletes the current view from the dictionary. :)) 
    '''
    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.exit_bar = ttk.Button(self, text="EXIT", command = lambda: ViewManager.instance.pop())
        self.exit_bar.grid(sticky="S")

