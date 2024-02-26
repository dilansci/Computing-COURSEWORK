import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager

class StaffSelectView(ttk.Frame):

    def __init__(self, master, all_teachers_view, all_assistants_view, **kargs):
        super().__init__(master, **kargs)
        self.all_teachers = all_teachers_view
        self.all_assistants = all_assistants_view
        ViewManager.instance.register_view(self, "StaffSelectView")
    
    def select_staff(self):
        ViewManager.instance.show_view("StaffSelectView")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.teacher_btn  = tk.Button(self, text="Teachers", height=10, width=20, command= lambda: [ViewManager.instance.hide_view(self), self.all_teachers.populate_teachers()])
        self.teacher_btn.grid(row=0, column=0, sticky="NESW")
        self.assistant_btn = tk.Button(self, text="Assistants", height=10, width=20, command= lambda: [ViewManager.instance.hide_view(self), self.all_assistants.populate_assistants()])
        self.assistant_btn.grid(row=0, column=1, sticky="NESW")
