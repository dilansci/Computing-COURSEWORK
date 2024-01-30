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
        # array for attendance buttons
        self.markipliers = []

    def reg_layout(self, reg_pos, list_of_ids):
        # this shows the RegView when the reg_button is pressed.
        ViewManager.instance.show_view("RegisterView")
        for widget in self.winfo_children():
            widget.destroy()

        self.swimmer_names = self.reg_control.get_swimmer_name(list_of_ids[reg_pos])

        for i in range (0, len(self.swimmer_names)):
            # gridding each individual swimmer here
            self.swim_name = tk.Label(self, text=self.swimmer_names[i][0] +" "+ self.swimmer_names[i][1]).grid(row=i, column=0)

            self.markipliers.append(tk.Button(self, text="Absent", background="red")) # will make command to change the attendance of swimmer in DB and colour :))
            self.markipliers[i].grid(row=i, column=5, columnspan=5)
        print("Current Reg_num",reg_pos,"and ID list",list_of_ids)
        self.markipliers.clear()

# make a function which makes a sql query that updates the Register table with the corresponding class_IDs.

'''
This view will contain the contents of each reg_button within 'day_view'
and display the appropriate data correlating to each 'register' i.e. class info.

'''