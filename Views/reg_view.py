import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager

class RegisterView(ttk.Frame):
    # Ideally this will clear the entire frame and put in the 'RegisterView'
    def __init__(self, master, control, **kargs):
        super().__init__(master, **kargs)
        # SINGLETON
        ViewManager.instance.register_view(self, "RegisterView")

        self.reg_control = control
        # array for Attendance buttons :))
        self.markipliers = []

    def reg_layout(self, reg_pos, list_of_ids):
        ViewManager.instance.show_view("RegisterView")
        
        for widget in self.winfo_children():
            widget.destroy()

        self.swimmer_names = self.reg_control.get_swimmer_name(list_of_ids[reg_pos])
        print(self.swimmer_names)
        for i in range (0, len(self.swimmer_names)):
            self.swim_name = tk.Label(self, text=self.swimmer_names[i][0] +" "+ self.swimmer_names[i][1]).grid(row=i, column=0)

            print("Markiplier",self.markipliers)
            self.markipliers.append(ttk.Button(self, text="Mark")) # will make command to change the attendance of swimmer in DB and colour :))
            self.markipliers[i].grid(row=i, column=1)
        print("Current Reg_num",reg_pos,"and ID list",list_of_ids)
        self.markipliers.clear()

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