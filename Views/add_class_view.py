import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager

class AddClassView(ttk.Frame):

    def __init__(self, master, control, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "AddClassView")
        self.control = control

    