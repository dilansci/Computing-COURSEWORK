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
        print(self.views)

    def show_view(self, name):
        view = self.views.get(name)
        if view:
            self.view_stack.append(view)
            self.grid_view(view)
            
    
    def grid_view(self, view):
        view.grid(sticky="NESW")

    def pop(self):
        if len(self.view_stack) > 1:
            # problem with this. It keeps adding instances of DayView into the self.view_stack
            print("This is view_stack BEFORE",self.view_stack)
            view = self.view_stack.pop()
            self.hide_view(view)
            self.grid_view(self.view_stack[len(self.view_stack)-1])
            
    def hide_view(self, view):
        # the view parameter is the "self" within the respective view.
        view.grid_forget()

# doesnt work. Refer to DayView for rest of problem