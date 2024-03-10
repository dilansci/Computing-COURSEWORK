import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager

'''
This view will contain the contents of each reg_button within 'day_view'
and display the appropriate data correlating to each 'register' i.e. class info.
'''
class RegisterView(ttk.Frame):

    def __init__(self, master, control, header, **kargs):
        super().__init__(master, **kargs)
        # SINGLETON
        ViewManager.instance.register_view(self, "RegisterView")
        
        self.reg_control = control
        self.header = header
        # array for attendance buttons
        self.markipliers = []

    def reg_layout(self, reg_pos, list_of_ids):
        self.view_name = "Register"
        self.header.update_header(self.view_name)

        self.markipliers.clear()

        ViewManager.instance.show_view("RegisterView")
        for widget in self.winfo_children():
            widget.destroy()
            
        curr_class_id = list_of_ids[reg_pos]
        self.swimmer_names = self.reg_control.get_swimmer_name(curr_class_id)
        self.swim_attendance = self.reg_control.get_attendance(self.swimmer_names)

        for i in range (0, len(self.swimmer_names)): 
            # gridding each individual swimmer here
            full_name = (self.swimmer_names[i][0] +" "+ self.swimmer_names[i][1])
            self.swim_name = tk.Label(self, text= full_name).grid(row=i, column=0)

            if self.swim_attendance[i]== 0:
                state = "Absent"
                pres_colour = "red"
            else:
                state = "Present"
                pres_colour = "green"
            self.markipliers.append(tk.Button(self, text=state, background=pres_colour, command= lambda index = i:
                                              self.attendance(index)))
            self.markipliers[i].grid(row=i, column=5, sticky="E")

            self.mark_swimmer = ttk.Button(self, text="MARK") # NO COMMAND YET!
            self.mark_swimmer.grid(row=i, column=6, sticky="E")

    def attendance(self, index):
        self.swim_attendance = self.reg_control.get_attendance(self.swimmer_names)
        # here the current "presence" of each swimmer should be updated. Each swimmer will start off as '0' (Absent). At the beginning of the week.
        self.curr_btn = self.markipliers[index]
        if self.curr_btn["text"] == "Absent":
            self.curr_btn["text"] = "Present"
            self.curr_btn["background"] = "green"
            self.reg_control.set_attendance(self.swimmer_names[index], self.swim_attendance[index])
        else:
            self.curr_btn["text"] = "Absent"
            self.curr_btn["background"] = "red"
            self.reg_control.set_attendance(self.swimmer_names[index], self.swim_attendance[index])