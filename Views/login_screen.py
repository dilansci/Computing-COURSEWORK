import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager
class LoginScreen(ttk.Frame):

    def __init__(self, master, control, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "LoginScreen")

        self.control = control
        self.view_name = "Login"
    
    def login_layout(self, user_access):
        ViewManager.instance.show_view("LoginScreen")
        print("DIS ONE",user_access)
        self.pin_box = ttk.Entry(self)
        self.pin_box.grid()
