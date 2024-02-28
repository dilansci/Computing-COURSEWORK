import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Widgets.scroll_widgets import *
from Views.view_manager import ViewManager

class DayView(ttk.Frame):

    def __init__(self, master, control, reg_view, sow_view, staff_select_view, class_view, header, **kargs): # using 'control' as a parameter is a short term fix. REMOVE ASAP!!!
        super().__init__(master, **kargs)
        # SINGLETON
        ViewManager.instance.register_view(self, "DayView")
        # declaring parameters
        self.control = control
        self.reg_view = reg_view
        self.sow_view = sow_view
        self.header = header
        self.staff_select_view = staff_select_view
        self.class_view = class_view
        # arrays
        self.registers = []
        self.class_ids = []
        self.class_contents = []
        self.sow_contents = []

        self.view_name = "Class Select"

    def day_layout(self, access_level, teacher_name):
        self.header.update_header(self.view_name)

        ViewManager.instance.show_view("DayView")
        for widget in self.winfo_children():
            widget.destroy()
            
        self.access_level = access_level
        self.display_name = teacher_name
        
        self.days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        self.day_buttons = []
        for i in range (len(self.days)):
            self.rowconfigure(0, weight=1)
            self.columnconfigure(i, weight=1)
            # This section assigns each button a 'name'. The button is then created and gridded.
            self.day_buttons.append(ttk.Button(self, text=self.days[i], command= lambda i=i: self.share_day(self.days[i]) ))
            self.day_buttons[i].grid(row=0,column=i, sticky="EW", pady=5) # DONT USE PAKCING!!! - matthew :)
        # Defaults the day to 'Monday'
        self.reg_widgets("Monday")
        self.other_widgets()

    def other_widgets(self):
        # Add teacher buttons here
        self.add_btn_frame = tk.Frame(self)
        self.add_btn_frame.grid()

        self.add_teacher_btn = ttk.Button(self.add_btn_frame, text="View Staff", command= lambda: [ViewManager.instance.hide_view(self), self.staff_select_view.select_staff()])
        self.add_teacher_btn.grid()
        # Prohibits Teachers and Assisstants from Adding Teachers/Classes
        if self.access_level != 0:
            self.add_teacher_btn.config(state="disabled")

    def share_day(self, day):
        self.kill_everything() # this always goes first :))
        self.reg_widgets(day)
        self.other_widgets()

    def reg_widgets(self, day):
        # self.header.update_header(self.view_name)
        self.class_ids.clear()
        # VerticalScrolledFrame uses 'self.reg_frame.interior' 
        self.reg_frame = VerticalScrolledFrame(self)
        self.reg_frame.grid(columnspan=8,sticky="NESW")

        self.reg_info = self.control.get_lessons_day(day)

        for count in range (0,len(self.reg_info)):
            r = count + 2   
            # Variables which fetch ALL necessary info
            self.sow = self.control.get_sow(self.reg_info[count][2])
            self.class_info = self.control.get_class(self.reg_info[count][1])
            print("Class info",self.class_info)

            # tracking class_ids for each reg_button
            self.current_id = self.class_info[0][1]
            self.current_class_id = self.class_info[0][0]
            self.class_ids.append(self.current_class_id)
            print("THE CURRENT CLASS_ID",self.current_class_id)
            # Class Info Components
            self.teacher_name = self.control.get_teacher_name(self.class_info[0][1])
            self.full_name = self.teacher_name[0][0] + " " + self.teacher_name[0][1]
            self.level_num = self.class_info[0][2]
            self.time = self.class_info[0][3]
            # Reg Buttons
            self.registers.append(ttk.Button(self.reg_frame.interior, text=f"Register {count+1}", command= lambda count_id = count: [ViewManager.instance.hide_view(self), self.reg_view.reg_layout(count_id, self.class_ids)]))
            self.registers[count].grid(row=r, column=0, sticky="EW")
            # Info
            self.class_contents.append(ttk.Label(self.reg_frame.interior, text=f"Teacher: {self.full_name}\t Level: {self.level_num}\t Time: {self.time}"))
            self.class_contents[count].grid(row=r, column=1, columnspan=3)
            # SOW Buttons
            self.sow_contents.append(ttk.Button(self.reg_frame.interior, text="SOW", command= lambda level_num_id = self.level_num: [ViewManager.instance.hide_view(self), self.sow_view.sow_layout(level_num_id)]))
            self.sow_contents[count].grid(row=r, column=6, sticky="NE")
            # EditClass Buttons
            # pass into the command the details of the class. i.e. Day, SOW, Class_info (this comes with teacher_id, level_num), Time (incase teacher)
            self.add_class_btn = ttk.Button(self.reg_frame.interior, text="Edit Classes", command= lambda teacher_id = self.current_id, time = self.time, level_num = self.level_num, curr_class_id = self.current_class_id: [ViewManager.instance.hide_view(self), self.class_view.show_classes(day, teacher_id, time, level_num, curr_class_id)]) # get SOW from sow_service
            self.add_class_btn.grid(row=r, column=7, sticky="NE")
            if self.access_level != 0:
                self.add_class_btn.config(state="disabled")

        # '.clear()' avoid crashing
        self.registers.clear()
        self.class_contents.clear()
        self.sow_contents.clear()

    def kill_everything(self):
        self.reg_frame.destroy()
        self.add_btn_frame.destroy()