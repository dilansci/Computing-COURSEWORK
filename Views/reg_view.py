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
        self.markipliers.clear()
        # this shows the RegView when the reg_button is pressed.
        ViewManager.instance.show_view("RegisterView")
        for widget in self.winfo_children():
            widget.destroy()

        self.swimmer_names = self.reg_control.get_swimmer_name(list_of_ids[reg_pos])
        print("ALL SWIMMERS",self.swimmer_names)
        # print("FIRST SWIMMER",self.swimmer_names[0])
        # print("FIRST SWIMMER'S first_name",self.swimmer_names[0][0])
        self.swim_attendance = self.reg_control.get_attendance(self.swimmer_names)
        print("ALL ATTENDANCE",self.swim_attendance)

        for i in range (0, len(self.swimmer_names)): 
            # gridding each individual swimmer here
            whole_name = (self.swimmer_names[i][0] +" "+ self.swimmer_names[i][1])
            self.swim_name = tk.Label(self, text= whole_name).grid(row=i, column=0)
            # make a sql query which checks the attendance in the DB and updates the button to that value.
            if self.swim_attendance[i]== 0:
                presence = "Absent"
                pres_colour = "red"
            else:
                presence = "Present"
                pres_colour = "green"
            self.markipliers.append(tk.Button(self, text=presence, background=pres_colour, command= lambda index = i: self.attendance(index))) # will make command to change the attendance of swimmer in DB and colour :))
            self.markipliers[i].grid(row=i, column=5, columnspan=5)

    def attendance(self, index):
        # here the current "presence" of each swimmer should be updated. Each swimmer will start off as '0' (Absent).
        # call self.set_attendance here passing in 'swimmer_names' and 'data_on_presence'
        self.curr_btn = self.markipliers[index]
        if self.curr_btn["text"] == "Absent":
            self.curr_btn["text"] = "Present"
            self.curr_btn["background"] = "green"
        else:
            self.curr_btn["text"] = "Absent"
            self.curr_btn["background"] = "red"


        # this function will change the colour of the button as well as update the attendance on the DB.
        '''
        Might need to make a new function for absent again
        btn1["text"] = "Power 1 On"
        btn1["fg"] = "green"
        '''


# make a function which makes a sql query that updates the Register table with the corresponding class_IDs.

'''
This view will contain the contents of each reg_button within 'day_view'
and display the appropriate data correlating to each 'register' i.e. class info.

'''