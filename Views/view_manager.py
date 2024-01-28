# Views/view_manager.py
import tkinter as tk

class ViewManager:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ViewManager, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

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
            view.grid()
