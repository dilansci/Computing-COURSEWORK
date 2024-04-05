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
        self.views[name] = view

    def show_view(self, name):
        view = self.views.get(name)
        if view:
            self.view_stack.append(view)
            self.grid_view(view)

    def grid_view(self, view):
        view.grid(sticky="NESW")

    def pop(self):
        if len(self.view_stack) > 1:
            view = self.view_stack.pop()
            self.hide_view(view)
            self.grid_view(self.view_stack[len(self.view_stack)-1])
            return view
        else:
            messagebox.showerror("Error","No view to go back to!")
            print("TRYING TO POP WITHOUT VIEW IN STACK!!!")
            
    def hide_view(self, view):
        # the view parameter is the "self" within the respective view.
        view.grid_forget()
    
    def refresh_view(self):
        # this will simply register the view again and pop it out of the stack, acting like the view simply refreshed.
        curr_view_name = self.views[self.view_stack]
        self.register_view(self.view_stack[0], curr_view_name)
        self.pop()