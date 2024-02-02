import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Widgets.scroll_widgets import *
from Views.view_manager import ViewManager

class DayView(ttk.Frame):

    def __init__(self, master, control, reg_view, sow_view, **kargs): # using 'control' as a parameter is a short term fix. REMOVE ASAP!!!
        super().__init__(master, **kargs)
        # SINGLETON
        ViewManager.instance = ViewManager()
        ViewManager.instance.instance.register_view(self, "DayView")
        # declaring the controller as 'self.control'
        self.control = control
        self.reg_view = reg_view
        self.sow_view = sow_view
        # arrays
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

    def share_day(self, day):
        self.kill_everything() # this always goes first :))
        self.reg_widgets(day)

    def reg_widgets(self, day):
        self.class_ids.clear()
        # VerticalScrolledFrame uses 'self.reg_frame.interior' 
        self.reg_frame = VerticalScrolledFrame(self)
        self.reg_frame.grid(columnspan=7,sticky="NESW")

        self.reg_info = self.control.get_lessons_day(day)

        for count in range (0,len(self.reg_info)):
            r = count + 2   
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
            self.registers.append(ttk.Button(self.reg_frame.interior, text=f"Register {count+1}", command= lambda count_id = count: [ViewManager.instance.hide_view(self), self.reg_view.reg_layout(count_id, self.class_ids)]))
            self.registers[count].grid(row=r, column=0, sticky="EW")
            # Info
            self.class_contents.append(ttk.Label(self.reg_frame.interior, text=f"Teacher: {self.teacher_name[0][0]} {self.teacher_name[0][1]}\t Level: {self.level_num}\t Time: {self.time}"))
            self.class_contents[count].grid(row=r, column=1, columnspan=3)
            # SOW Buttons
            self.sow_contents.append(ttk.Button(self.reg_frame.interior, text="SOW", command= lambda level_num_id = self.level_num: [ViewManager.instance.hide_view(self), self.sow_view.sow_layout(level_num_id)])) # command should go to 'sow_view' file and display the sow details
            self.sow_contents[count].grid(row=r, column=6, columnspan=3, sticky="NE")

        # '.clear()' avoid crashing
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