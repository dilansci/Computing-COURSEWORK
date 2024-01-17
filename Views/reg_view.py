import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Widgets.scroll_widgets import *

class RegisterView(ttk.Frame):
    # Ideally this will clear the entire frame and put in the 'RegisterView'
    def __init__(self, master, control, **kargs):
        super().__init__(master, **kargs)
        self.control = control
    
    def reg_layout(self, reg_pos, list_of_ids):
        print("Current Reg_num",reg_pos,"and ID list",list_of_ids)

        # make a function which makes a sql query that updates the Register table with the corresponding class_IDs.

        '''
        This view will contain the contents of each reg_button within 'day_view'
        and display the appropriate data correlating to each 'register' i.e. class info.
        '''