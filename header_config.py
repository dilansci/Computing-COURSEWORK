import tkinter as tk
from tkinter import ttk

# this class which eventually be able to change the header shown depending on what functionality is being used i.e
# if in register section it will display "Lesson Manager - Register".
class Header(ttk.Frame):
    # header is a labelframe
    # 'header' class will constantly update the location in which the user is accessing.
    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.head_label = ttk.Label(self, text="Lesson Manager")
        self.head_label.grid(row=0, column=0)
        self.head_list = []

    def update_header(self, name):
        self.head_list.append(name)
        self.head_label["text"] = "Lesson Manager - " + name
    
    def on_exit(self):
        if len(self.head_list) > 1:
            self.head_list.pop()
            self.head_label["text"] = "Lesson Manager - " + self.head_list[-1]
            print("CUrrent View list", self.head_list)
        elif len(self.head_list) == 1:
            self.head_list.pop()
            self.head_label["text"] = "Lesson Manager"