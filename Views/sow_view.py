import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager
from Widgets.scroll_widgets import *


class SOWView(ttk.Frame):

    def __init__(self, master, control, **kargs):
        super().__init__(master,**kargs)
        # SINGLETON
        ViewManager.instance.register_view(self, "SOWView")

        self.sow_control = control
    # will make a list of buttons for each level 1-7 and have them output the SOW when each is pressed.
    def sow_layout(self, level_num): # will need to implement week num into this
        ViewManager.instance.show_view("SOWView")

        self.sow_info = self.sow_control.get_sow_level(level_num)
        
        print("This is the level num",level_num)
        print("Details for this level",self.sow_info)

    def tree_views(self):
        self.column_names = ("Intro", "Main", "Contrast") 
        self.reg_tree = ttk.Treeview(self.reg_frame.interior, columns=self.column_names, show="headings")
        self.reg_tree.heading("Intro", text="Intro")
        self.reg_tree.heading("Main", text="Main")
        self.reg_tree.heading("Contrast",text="Contrast")
        # print("CLass content values TREE",self.class_contents)

        for each_class in self.class_contents:
                print("EACH_CLASS",each_class)
                self.reg_tree.insert('', 1, values=each_class)
        self.class_contents.clear()

        self.reg_tree.grid(row=2, rowspan=10, column=1, sticky="NESW")







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