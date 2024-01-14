import tkinter as tk
from tkinter import ttk
# from Controllers.reg_controller import RegController

class RegisterView(ttk.Frame):
    # Ideally this will clear the entire frame and put in the 'RegisterView'
    def __init__(self, master, control, **kargs):
        super().__init__(master, **kargs)
        self.control = control
        print("This is RegControl!",self.control)

        '''
        This view will contain the contents of each reg_button within 'day_view'
        and display the appropriate data correlating to each 'register' i.e. class info.
        '''