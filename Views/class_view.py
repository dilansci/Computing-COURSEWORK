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
    def show_classes(self, day, level, all_teachers, teacher_id):
        self.header.update_header(self.view_name)

        self.day = day
        self.level = level
        self.all_teacher = all_teachers
        self.teacher_id = teacher_id

        ViewManager.instance.show_view("ClassView")
        for widget in self.winfo_children():
            widget.destroy()
        
        # self.all_classes = self.control.get_class()
        # print("ALL CLASS INFO",self.all_classes)
        print(day)
        print(level)
        print(teacher)
        