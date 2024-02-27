import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager

class ClassView(ttk.Frame):

    def __init__(self, master, control, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "ClassView")
        self.control = control
        self.header = header

        self.view_name = "Classes"

    # use swimmerService like in "day_view"
    def show_classes(self, day, teacher_id, time):
        self.header.update_header(self.view_name)

        ViewManager.instance.show_view("ClassView")
        for widget in self.winfo_children():
            widget.destroy()
        
        self.day = day
        self.teacher_id = teacher_id
        self.time = time
        print("TEACHER ID",self.teacher_id)

        # self.swimmer_names = self.control.get_swimmer_name(list_of_ids[reg_pos])
        

        