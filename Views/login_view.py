import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager

class LoginView(ttk.Frame):

    def __init__(self, master, control, day_view **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance = ViewManager()
        ViewManager.instance.instance.register_view(self, "LoginView")
        # declaring parameters
        self.control = control
        self.day_view = day_view

        self.view_name = "Login"
        self.login_choice = ["Manager","Teacher","Assistant"]

        for i in range (len(self.login_choice)):
            self.login_button = tk.Button(self,text=self.login_choice[i], height=10, width=20, command= lambda user_access=i: [ViewManager.instance.hide_view(self), self.day_view.day_layout(user_access)])
            self.login_button.grid(row=0,column=i,sticky="NESW")
            ## might have it so that the user_access is passed into every single view
    def share_access(self, access_level):
        print("Your access level is",access_level)