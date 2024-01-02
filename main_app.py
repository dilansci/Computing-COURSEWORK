import tkinter as tk
from tkinter import ttk
from header_config import *
from register import *
from Views.day_view import DayView
from Views.reg_view import RegisterView

class Main(tk.Tk):

    # creating a class which acts as a dictionary for all the contents of the registry.
    def __init__(self):
        super().__init__()
        self.title("SwimmerDB")
        self.geometry("600x500")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # most of the code/widgets will be stored with the 'self.container' frame.
        self.container = tk.LabelFrame(self)

        # this is the frame where the header from 'header_config' will be displayed.
        self.header = Header(self.container)
        self.header.grid(row=0, column=0, padx=5, pady=5, sticky="NEW")

        # specifiying the area where the 'container' frame is packed within 'Main'.
        self.container.columnconfigure(0, weight=1)

        self.container.grid(sticky="NESW", padx=5, pady=5)

        # this is the frame which will contain all the Days from 'day_view'
        self.d_view = DayView(self.container)
        self.d_view.grid(row=1, column=0, padx=5, pady=5)

        # self.r_view = RegisterView(self.container)
        # self.r_view.grid(row=2, column=0, padx=5, pady=5) # did a good :)

if __name__ == '__main__':
    main = Main()
    main.mainloop()