import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager
from account_manager import AccountManager

class LoginView(ttk.Frame):

    def __init__(self, master, control, login_screen, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "LoginView")
        # declaring parameters
        self.control = control
        self.login_screen = login_screen

        self.view_name = "Login"
        self.login_choice = ["Manager","Teacher","Assistant"]

        for i in range (len(self.login_choice)):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
            self.login_button = tk.Button(self,text=self.login_choice[i], height=10, width=20, command= lambda user_access=i: [ViewManager.instance.hide_view(self) ,self.login_screen.login_layout(user_access)]) #[ViewManager.instance.hide_view(self), self.day_view.day_layout(user_access)]
            self.login_button.grid(row=0,column=i,sticky="NESW")
