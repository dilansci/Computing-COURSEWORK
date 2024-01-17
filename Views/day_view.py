import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Widgets.scroll_widgets import *

from Views.reg_view import RegisterView

class DayView(ttk.Frame):

    def __init__(self, master, control, **kargs): # using 'control' as a parameter is a short term fix. REMOVE ASAP!!!
        super().__init__(master, **kargs)
        # declaring the controller as 'self.control'
        self.control = control
        # temp arrays
        self.registers = []
        self.class_ids = []
        self.class_contents = []
        self.sow_contents = []
        # this iterates through each day Mon-Sun and creates a button.
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.day_buttons = []

        for i in range (len(self.days)):
            self.rowconfigure(0, weight=1)
            self.columnconfigure(i, weight=1)
            # this section assigns each button a 'name'. The button is then created and gridded.
            self.day_buttons.append(ttk.Button(self, text=self.days[i], command= lambda i=i: self.share_day(self.days[i]) ))
            self.day_buttons[i].grid(row=0,column=i, sticky="EW", pady=5) # DONT USE PAKCING!!! - matthew :)
        self.reg_widgets("Monday")
        # self.tree_views()

    def share_day(self, day):
        self.kill_everything() # this always goes first :))
        self.reg_widgets(day)
        # self.tree_views()
    '''UNSURE IF I SHOULD KEEP "TREE_VIEW". MIGHT IMPLEMENT IN POST PROTOTYPE REFINEMENT!'''
    # def tree_views(self):
    #     self.column_names = ("Teacher", "Level", "Time") 
    #     self.reg_tree = ttk.Treeview(self.reg_frame.interior, columns=self.column_names, show="headings")
    #     self.reg_tree.heading("Teacher", text="Teacher")
    #     self.reg_tree.heading("Level", text="Level")
    #     self.reg_tree.heading("Time",text="Time")    
    #     print("CLass content values TREE",self.class_contents)

    #     for each_class in self.class_contents:
    #             print("EACH_CLASS",each_class)
    #             self.reg_tree.insert('', 1, values=each_class)
    #     self.class_contents.clear()

    #     self.reg_tree.grid(row=2, rowspan=10, column=1, sticky="NESW")

    def reg_widgets(self, day):
        self.class_ids.clear()
        # VerticalScrolledFrame uses 'self.reg_frame.interior' 
        self.reg_frame = VerticalScrolledFrame(self)
        self.reg_frame.grid(columnspan=7,sticky="NESW")

        self.reg_info = self.control.get_lessons_day(day)

        r = 2   
        for count in range (0,len(self.reg_info)):
            # Variables which fetch ALL necessary info
            self.sow = self.control.get_sow(self.reg_info[count][2]) 
            # make this into an array of buttons and place them beside respective registers (think about this you need to track which reg are which)
            self.class_info = self.control.get_class(self.reg_info[count][1])

            # tracking class_ids for each reg_button
            self.current_id = self.class_info[0][0]
            self.class_ids.append(self.current_id)
            # Class Info Components
            self.teacher_name = self.control.get_teacher_name(self.class_info[0][1])
            self.level_num = self.class_info[0][2]
            self.time = self.class_info[0][3]
            # Reg Buttons
            self.registers.append(ttk.Button(self.reg_frame.interior, text=f"Register {count+1}", command= lambda count_id = count: RegisterView.reg_layout(self, count_id, self.class_ids)))
            self.registers[count].grid(row=r, column=0, sticky="EW")
            # Info
            self.class_contents.append(ttk.Label(self.reg_frame.interior, text=f"Teacher: {self.teacher_name[0][0]} {self.teacher_name[0][1]}\t Level: {self.level_num}\t Time: {self.time}"))
            self.class_contents[count].grid(row=r, column=1, columnspan=3)
            # Syllabus
            self.sow_contents.append(ttk.Button(self.reg_frame.interior, text="Syllabus")) # command should go to 'sow_view' file and display the sow details
            self.sow_contents[count].grid(row=r, column=6, columnspan=3, sticky="NE")
            r += 1
        # '.clear()' each of the temp arrays to avoid crashing
        self.registers.clear()
        self.class_contents.clear()
        self.sow_contents.clear()

    def kill_everything(self):
        self.reg_frame.destroy()

'''
Lesson --> class_ID --> teacher_ID -->
                    --> level_num
                        --> syllabus
'''