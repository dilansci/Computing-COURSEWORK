import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Widgets.scroll_widgets import *

class DayView(ttk.Frame):

    def __init__(self, master, control, **kargs): # using 'control' as a parameter is a short term fix. REMOVE ASAP!!!
        super().__init__(master, **kargs)
        # declaring the controller as 'self.control'
        self.control = control
        print("This is DayControl!",self.control)
        # create widgets here
        # buttons
        self.registers = []
        self.class_contents = []
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.day_buttons = []
        
        # this iterates through each day Mon-Sun and creates a button.
        for i in range (len(self.days)):
            self.rowconfigure(0, weight=1)
            self.columnconfigure(i, weight=1)
            # this section assigns each button a 'name'. The button is then created and gridded.
            self.day_buttons.append(ttk.Button(self, text=self.days[i], command= lambda i=i: self.share_day(self.days[i]) ))
            self.day_buttons[i].grid(row=0,column=i, sticky="EW", pady=5) # DONT USE PAKCING!!! - matthew :)
        self.reg_widgets("Monday")

    def share_day(self, day):
        self.kill_everything() # this always goes first :))
        self.reg_widgets(day)
        

    def reg_widgets(self, day):
        ## VerticalScrolledFrame uses 'self.reg_frame.interior' 
        self.reg_frame = VerticalScrolledFrame(self)
        self.reg_frame.grid(columnspan=7,sticky="NESW") # columnspan makes the entire frame occupy from Mon-Sun.

        reg_info = self.control.day_service.get_lessons_day(day) 
        print("Class count",reg_info)

        r = 2
        for count in range (0,len(reg_info)):
            print(count)
            self.class_info = self.control.get_class(reg_info[count][1]) ## Recreate service functions inside respective controllers. i.e. self.control.get_class --> (SERVICE) self.service.get_class
            print("Class info", self.class_info)
            self.teacher_name = self.control.reg_service.get_teacher_name(self.class_info[0][1])
            print(self.teacher_name)
            self.level_num = self.class_info[0][2]
            print("Current Level num", self.level_num)
            # Reg Buttons
            self.registers.append(ttk.Button(self.reg_frame.interior, text=f"Register {count+1}")) # will give command soon   
            self.registers[count].grid(row=r, column=0, sticky="EW")
            # Info
            self.class_contents.append(ttk.Label(self.reg_frame.interior, text=f"Teacher: {self.teacher_name[0][0]} {self.teacher_name[0][1]}")) # call class_contents
            self.class_contents[count].grid(row=r, column=1, columnspan=2, sticky="NESW")
            # when sticky="NESW" it expands the button to be the size of the row. Could use this for the labels to display info on each class within the Register.
            r += 1
        self.registers.clear()
        self.class_contents.clear()

    def tree_views(self):
        self.column_names = ("Teacher", "Level", "Time") 
        self.reg_tree = ttk.Treeview(self, columns=self.column_names, show="headings")
        self.reg_tree.heading("Teacher", text= (self.teacher_name[0][0] + self.teacher_name[0][1]))
        self.reg_tree.heading("Level", text=self.class_info[0][2])
        self.reg_tree.heading("Time",text=)

    def kill_everything(self):
        self.reg_frame.destroy()

'''
Lesson --> class_ID --> teacher_ID -->
                    --> level_num
                        --> syllabus
'''