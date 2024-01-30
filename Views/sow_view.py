import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager


class SOWView(ttk.Frame):

    def __init__(self, master, control, **kargs):
        super().__init__(master,**kargs)
        # SINGLETON
        ViewManager.instance.register_view(self, "SOWView")

        self.sow_control = control
    # will make a list of buttons for each level 1-7 and have them output the SOW when each is pressed.
    def sow_layout(self, level_num):
        ViewManager.instance.show_view("SOWView")
        print("This is the level num",level_num)
'''
SOWView will display the SOW for the set week (Week 1). 
Should implement code for DayView into here as it will be the same principal.
Week 1 --> Level 1 (week 1)
           Level 2  ...
           Level 3  ...
           level 4  ...
           level 5  ...
           level 6  ...
           level 7  ...
Week 2 --> Level 1 (week 2)
'''