import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager

class ClassView(ttk.Frame):

    def __init__(self, master, control, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "AddClassView")
        self.control = control
        self.header = header

        self.view_name = "Classes"

        # will contain an option to add class/add new swimmers for the class. Here a teacher is assigned. mIght implement add teacher functionality into this view ;))
    def class_layout(self):
        self.header.update_header(self.view_name)
        

    