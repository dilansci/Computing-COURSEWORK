# Views/view_manager.py
import tkinter as tk
from tkinter import messagebox

class ViewManager:
    instance = None

    def __init__(self):
        if self.__class__.instance == None:
            self.__class__.instance = self

        self.views = {}
        self.view_stack = []

    def register_view(self, view, name):
        # the 'name' will always be loginview as it is the last called view in 'main.py'!
        self.views[name] = view

    def show_view(self, name):
        view = self.views.get(name)
        print("SHOW",view)
        if view:
            self.view_stack.append(view)
            self.grid_view(view)

    def grid_view(self, view):
        view.grid(sticky="NESW")

    def pop(self):
        if len(self.view_stack) > 1:
            view = self.view_stack.pop()
            self.hide_view(view)
            self.grid_view(self.view_stack[-1])
            return view
        else:
            messagebox.showerror("Error","No view to go back to!")
            print("TRYING TO POP WITHOUT VIEW IN STACK!!!")

    def hide_view(self, view):
        # the view parameter is the "self" within the respective view.
        view.grid_forget()     

    def refresh_pop(self):
        print("refresh pop")
        if len(self.view_stack) > 1:
            view = self.view_stack.pop()
            self.hide_view(view)


        
