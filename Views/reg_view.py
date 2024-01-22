import tkinter as tk
from tkinter import ttk

class RegisterView(ttk.Frame):
    # Ideally this will clear the entire frame and put in the 'RegisterView'
    def __init__(self, master, control, **kargs):
        super().__init__(master, **kargs)
        self.reg_control = control # reg_controller
        print("This is Register Controller", self.reg_control)
    
    def reg_layout(self, reg_pos, list_of_ids):
        self.destroy() 

        '''
        Might implement a SEPERATE FILE which gets called when a different view is accessed
        i.e. (Initial view) --> clear_window --> (Next View)
        Would I need a 'clear_controller' for this??
        '''

        print("Current Reg_num",reg_pos,"and ID list",list_of_ids)
        swimmer_names = self.reg_control.get_swimmer_name(list_of_ids[reg_pos]) # error here. prob because of 'day_view' line 75 ://. Im passing 'self' which i think is wrong
        print(swimmer_names)



        # make a function which makes a sql query that updates the Register table with the corresponding class_IDs.

        '''
        This view will contain the contents of each reg_button within 'day_view'
        and display the appropriate data correlating to each 'register' i.e. class info.
        '''