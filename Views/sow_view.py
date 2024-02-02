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
        for widget in self.winfo_children():
            widget.destroy()

        self.sow_info = self.sow_control.get_sow_level(level_num)
        
        print("This is the level num",level_num)
        print("Details for this level",self.sow_info)

    # def tree_views(self):
        self.column_names = ("Intro", "Main", "Contrast", "Depth") 
        self.reg_tree = ttk.Treeview(self, columns=self.column_names, show="headings")
        self.reg_tree.heading("Intro", text="Intro")
        self.reg_tree.column("Intro", width=100)
        self.reg_tree.heading("Main", text="Main")
        self.reg_tree.column("Main", width=250) # width=250 give 50 characters worth of space (5 : 1) ratio
        self.reg_tree.heading("Contrast",text="Contrast")
        self.reg_tree.heading("Depth",text="Depth")
        self.reg_tree.column("Depth", width=40)

        self.main_temp = []
        self.rowconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        for each_sow in self.sow_info:
                print("Length",len(each_sow[1]))
                if len(each_sow[1]) > 40:
                     new_slice = each_sow[1]
                     old_slice = each_sow # have to make a variable to hold the remaining parts of 'each_sow[1]' (main)
                     # have to convert the tuple 'each_sow' into a list for slicing
                    #  new_list = list(each_sow)
                    #  new_list[1] = new_slice[0:40]
                    #  print("NEW LIST",new_list)
                    #  print("Sliced version",new_slice[0:40])
                print("EACH_CLASS",each_sow[1])
                self.reg_tree.insert('', 1, values=each_sow)
                self.reg_tree.insert('', 2, values=("","Heyyy","",""))
                # somehow track the length of each parameter and create a new line to prevent it extending onwards.
        self.sow_info.clear()

        self.reg_tree.grid(row=0, column=1, sticky="NEW")







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