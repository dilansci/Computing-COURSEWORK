# Views/view_manager.py
import tkinter as tk

class ViewManager:
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = super(ViewManager, cls).__new__(cls)
            cls.instance._initialized = False
        return cls.instance

    def __init__(self):
        if not self._initialized:
            self.views = {}
            self.view_stack = []
            self._initialized = True

    def register_view(self, view, name):
        self.views[name] = view

    def show_view(self, name):
        view = self.views.get(name)
        if view:
            self.view_stack.append(view)
            view.grid()

    def pop(self):
        if self.view_stack:
            view = self.view_stack.pop()
            self.hide_view(view)
            self.show_view(self.get_view_name(self.view_stack[len(self.view_stack)-1]))

    def get_view_name(self, view):
        for key,item in self.views.items():
            if view == item:
                return key
            

    def hide_view(self, view):
        # the view parameter is the "self" within the respective view.
        view.grid_forget()

# doesnt work. Refer to DayView for rest of problem