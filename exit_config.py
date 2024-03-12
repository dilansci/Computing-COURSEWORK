import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager

class Exit(tk.LabelFrame):

    def __init__(self, master, header, **kargs):
        super().__init__(master, **kargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.header = header
        
        self.exit_bar = ttk.Button(self, text="BACK", command = lambda: 
                                   [ViewManager.instance.pop(), self.header.on_exit()])
        self.exit_bar.grid(sticky="S")
