import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager

class RegisterView(ttk.Frame):
    # Ideally this will clear the entire frame and put in the 'RegisterView'
    def __init__(self, master, control, **kargs):
        super().__init__(master, **kargs)
        # SINGLETON
        view_manager = ViewManager()
        view_manager.register_view(self, "RegisterView")
        view_manager.show_view("RegisterView")
        self.reg_control = control # reg_controller
        print("This is Register Controller", self.reg_control)
    
    def reg_layout(self, reg_pos, list_of_ids):
        self.destroy()

        print("Current Reg_num",reg_pos,"and ID list",list_of_ids)
        swimmer_names = self.reg_control.get_swimmer_name(list_of_ids[reg_pos])
        print(swimmer_names)

        # make a function which makes a sql query that updates the Register table with the corresponding class_IDs.

        '''
        This view will contain the contents of each reg_button within 'day_view'
        and display the appropriate data correlating to each 'register' i.e. class info.
        '''
## IDEAS 
        

        '''
        Gonna implement new method of switching ViewFrames.
        - Make a stack of all the views starting with the Login,
          and have every other view in the stack hidden until called.
        - When a view is called, I will refer to the 'ViewManager' which will 
          contain the stack of views, and reveal the respective View (in turn
          hiding the current View).
        - When the 'Back' button is pressed, 'ViewManager' is accessed again
          and will revert the stack.
        
        
        '''

        '''
        Might implement a SEPERATE FILE which gets called when a different view is accessed
        i.e. (Initial view) --> clear_window --> (Next View)
        Would I need a 'clear_controller' for this??
        '''