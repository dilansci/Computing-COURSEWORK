import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Views.view_manager import ViewManager
from Widgets.scroll_widgets import *


class SOWView(ttk.Frame):

    def __init__(self, master, control, **kargs):
        super().__init__(master,**kargs)
        # SINGLETON
        ViewManager.instance.register_view(self, "SOWView")
        self.sow_control = control

    def sow_layout(self, sow_id): # will need to implement week num into this
        ViewManager.instance.show_view("SOWView")
        for widget in self.winfo_children():
            widget.destroy()

        self.sow_info = self.sow_control.get_sow(sow_id)

        r = 1
        # headings for SOW
        self.column_names = ("Intro", "Main", "Contrast", "Depth") 
        for i in range (0, len(self.column_names)):
             self.column_l = tk.Label(self, text=self.column_names[i]).grid(row=0, column=i)
        # length check for each SOW
        truncated_infos = []
        for sow in range (len(self.sow_info)):
            info = self.sow_info[sow]
            if len(self.sow_info[sow]) > 35:
                info = info[0:35] + "..." + info[35:-1]
            truncated_infos.append(info)
        # listboxes for SOW
        self.intro_box = tk.Listbox(self, width=30)
        self.intro_box.grid(row=r, column=0)
        self.intro_box.bind("<<ListboxSelect>>", self.callback)

        self.main_box = tk.Listbox(self, width=30)
        self.main_box.grid(row=r, column=1)
        self.main_box.bind("<<ListboxSelect>>", self.callback)

        self.contrast_box = tk.Listbox(self, width=30)
        self.contrast_box.grid(row=r, column=2)
        self.contrast_box.bind("<<ListboxSelect>>", self.callback)

        self.depth = tk.Listbox(self, width=10)
        self.depth.grid(row=r, column=3)
        # insert SOW
        self.intro_box.insert(0, truncated_infos[0])
        self.main_box.insert(0, truncated_infos[1])
        self.contrast_box.insert(0, truncated_infos[2])
        self.depth.insert(0, truncated_infos[3])
    
    def callback(self, event):
        # selects the listbox widget
        selection = event.widget.curselection()
        if selection:
            # declaring the index for the listbox to access
            index = selection[0] # this is just '0'
            data = (event.widget.get(index)).replace("...","")
            self.full_info = messagebox.showinfo("Info", data)

    



















        # self.reg_tree = ttk.Treeview(self, columns=self.column_names, show="headings", selectmode="none")
        # self.reg_tree.heading("Intro", text="Intro")
        # self.reg_tree.column("Intro", stretch=0)
        # self.reg_tree.heading("Main", text="Main")
        # self.reg_tree.column("Main", stretch=0)
        # self.reg_tree.heading("Contrast",text="Contrast")
        # self.reg_tree.column("Contrast", stretch=0)
        # self.reg_tree.heading("Depth",text="Depth")
        # self.reg_tree.column("Depth", stretch=0)
        # might just make 3 listboxes with an 'EDIT' button tied to each widget which unlocks them (for managers)

        # self.main_temp = []
        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(1, weight=1)
        # for each_sow in self.sow_info:
        #         self.reg_tree.insert('', 1, values=each_sow)
        #         self.reg_tree.insert('', 2, values=("","Heyyy","",""))
        #         # somehow track the length of each parameter and create a new line to prevent it extending onwards.
        #         # or just make the treeview column to resize itself when more characters are put ins
        # self.sow_info.clear()

        # self.reg_tree.grid(row=0, column=1, sticky="NEW")

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