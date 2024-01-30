import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager


class SOWView(ttk.Frame):

    def __init__(self, master, control, **kargs):
        super().__init__(master,**kargs)
        # SINGLETON
        ViewManager.instance.register_view(self, "SOWView")

        self.sow_control = control
