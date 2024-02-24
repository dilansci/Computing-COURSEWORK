import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager

class NewTeacherView(ttk.Frame):

    def __init__(self,master, control, **kargs): # add additional parameters
        super().__init__(master,**kargs)
        self.control = control
        ViewManager.instance.register_view(self, "NewTeacherView")
        '''
        This view will show entry widgets containing the info needed for a teacher
        e.g. Fname, Lname, Phone, Email, Pin etc
        Use SQL query to then UPDATE the DB with this info.
        NEED TO MAKE A FUNCTION FOR ADDING A TEACHER TO A CLASS!!! (same with adding a new class with swimmers) :)
        '''
    def new_teacher_layout(self):
        ViewManager.instance.show_view("NewTeacherView")
        label = tk.Label(self, text="YOUR IN THE ADD TEACHER MENU :))").grid()
        self.teacher_fname = ttk.Entry(self)
