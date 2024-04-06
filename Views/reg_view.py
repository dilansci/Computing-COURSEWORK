import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager

'''
This view will contain the contents of each reg_button within 'day_view'
and display the appropriate data correlating to each 'register' i.e. class info.
'''
class RegisterView(ttk.Frame):

    def __init__(self, master, control, assessment_view, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "RegisterView")
        
        self.reg_control = control
        self.assessment_view = assessment_view
        self.header = header

        self.attendance_buttons = []

    def reg_layout(self, reg_pos, list_of_ids):
        self.view_name = "Register"
        self.header.update_header(self.view_name)

        self.attendance_buttons.clear()

        ViewManager.instance.show_view("RegisterView")
        for widget in self.winfo_children():
            widget.destroy()
            
        self.curr_class_id = list_of_ids[reg_pos]
        self.swimmers_in_class = self.reg_control.get_swimmers_in_class(self.curr_class_id)
        self.swim_attendance = self.reg_control.get_attendance(self.curr_class_id)

        for i in range (0, len(self.swimmers_in_class)):
            # gridding each individual swimmer here
            full_name = (self.swimmers_in_class[i][1] +" "+ self.swimmers_in_class[i][2])
            curr_swimmer_id = self.swimmers_in_class[i][0]
            self.swim_name = tk.Label(self, text= full_name).grid(row=i, column=0)
            # changing the attributes of the button
            if self.swim_attendance[i]== 0:
                state = "Absent"
                pres_colour = "red"
            else:
                state = "Present"
                pres_colour = "green"
            self.attendance_buttons.append(tk.Button(self, text=state, background=pres_colour, command= lambda index = i:
                                              self.attendance(index)))
            self.attendance_buttons[i].grid(row=i, column=5, sticky="E")
            # Give each "MARK" button a 'swimmer_id'
            self.mark_swimmer = ttk.Button(self, text="MARK", command= lambda swimmer_id = curr_swimmer_id:
                                           [ViewManager.instance.hide_view(self), self.assessment_view.assessment_layout(swimmer_id, self.curr_class_id)])
            self.mark_swimmer.grid(row=i, column=6, sticky="E")

    def attendance(self, index):
        self.swim_attendance = self.reg_control.get_attendance(self.curr_class_id)
        # here the current "presence" of each swimmer should be updated. Each swimmer will start off as '0' (Absent). At the beginning of the week.
        self.curr_attendance = self.swim_attendance[index]
        self.curr_swimmer = self.swimmers_in_class[index][0]
        print("SWIMMER ID", self.curr_swimmer)
        
        self.curr_btn = self.attendance_buttons[index]
        if self.curr_btn["text"] == "Absent":
            self.curr_btn["text"] = "Present"
            self.curr_btn["background"] = "green"
            self.reg_control.set_attendance(self.curr_swimmer, self.curr_attendance)
        else:
            self.curr_btn["text"] = "Absent"
            self.curr_btn["background"] = "red"
            self.reg_control.set_attendance(self.curr_swimmer, self.curr_attendance)