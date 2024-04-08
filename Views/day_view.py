import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Widgets.scroll_widgets import *
from Views.view_manager import ViewManager

class DayView(ttk.Frame):

    def __init__(self, master, control, reg_view, sow_view, staff_select_view, class_view, all_classes_view, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "DayView")
        # declaring parameters
        self.control = control
        self.reg_view = reg_view
        self.sow_view = sow_view
        self.header = header
        self.staff_select_view = staff_select_view
        self.class_view = class_view
        self.all_classes_view = all_classes_view
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
            # This section assigns each button a 'name' from 'self.days'. The button is then created and gridded.
            self.day_buttons.append(ttk.Button(self, text=self.days[i], command= lambda day=i: self.share_day(self.days[day])))
            self.day_buttons[i].grid(row=0, column=i, sticky="EW", pady=5)
        # Defaults the day to 'Monday'
        self.reg_widgets("Monday")
        self.other_fncts()

    def other_fncts(self):
        # Add teacher buttons to this frame
        self.more_widgets_frame = ttk.Labelframe(self, text="Other functions")
        self.more_widgets_frame.grid(pady=10)

        self.view_staff_btn = ttk.Button(self.more_widgets_frame, text="View Staff", command= lambda: 
                                         [ViewManager.instance.hide_view(self), self.staff_select_view.select_staff()])
        self.view_staff_btn.grid(row=0, column=0, padx=5, pady=5)

        self.view_classes_btn = ttk.Button(self.more_widgets_frame, text="View Classes", command= lambda: [ViewManager.instance.hide_view(self), self.all_classes_view.classes_layout()])
        self.view_classes_btn.grid(row=0, column=1, padx=5, pady=5)
        # Prohibits Teachers and Assistants from Adding Teachers/Classes
        if self.access_level != 0:
            self.view_staff_btn.config(state="disabled")

    def share_day(self, day):
        self.destroy_everything() # call this first to clear widgets
        self.reg_widgets(day)
        self.other_fncts()

    def reg_widgets(self, day):
        self.class_ids.clear()
        # VerticalScrolledFrame uses 'self.reg_frame.interior' as it's frame
        self.reg_frame = VerticalScrolledFrame(self)
        self.reg_frame.grid(columnspan=8,sticky="NESW")

        self.reg_info = self.control.get_lessons_day(day)

        for count in range (len(self.reg_info)):
            r = count + 2   
            # Variables which fetch ALL necessary info
            self.sow_id = self.reg_info[count][2]
            self.sow = self.control.get_sow(self.sow_id)
            test = self.reg_info[count][1]
            self.class_info = self.control.get_class(self.reg_info[count][1])

            # tracking class_ids for each reg_button
            self.current_id = self.class_info[0][1]
            self.current_class_id = self.class_info[0][0]
            self.class_ids.append(self.current_class_id)
            # Class Info Components
            self.teacher_name = self.control.get_teacher_name(self.class_info[0][1])
            self.full_name = self.teacher_name[0][0] + " " + self.teacher_name[0][1]
            self.level_num = self.class_info[0][2]
            self.time = self.class_info[0][3]
            # Register Buttons
            self.registers.append(ttk.Button(self.reg_frame.interior, text=f"Register {count+1}", command= lambda count_id = count: 
                                             [ViewManager.instance.hide_view(self), self.reg_view.reg_layout(count_id, self.class_ids)]))
            self.registers[count].grid(row=r, column=0, sticky="EW")
            # Class Info
            self.class_contents.append(ttk.Label(self.reg_frame.interior, text=f"Teacher: {self.full_name}\t Level: {self.level_num}\t Time: {self.time}"))
            self.class_contents[count].grid(row=r, column=1, columnspan=3)
            # SOW Buttons
            self.sow_contents.append(ttk.Button(self.reg_frame.interior, text="SOW", command= lambda sow_id = self.sow_id: 
                                                [ViewManager.instance.hide_view(self), self.sow_view.sow_layout(sow_id)]))
            self.sow_contents[count].grid(row=r, column=6, sticky="NE")
            # Edit Class Buttons
            self.edit_class_btn = ttk.Button(self.reg_frame.interior, text="Edit Class", command= lambda class_id = self.current_class_id, teacher_id = self.current_id, sow_id = self.sow_id, level = self.level_num: 
                                            [ViewManager.instance.hide_view(self), self.class_view.show_classes(class_id, sow_id, teacher_id, level)])
            self.edit_class_btn.grid(row=r, column=7, sticky="NE")
            if self.access_level != 0:
                self.edit_class_btn.config(state="disabled")

        # '.clear()' avoid crashing
        self.registers.clear()
        self.class_contents.clear()
        self.sow_contents.clear()

    def destroy_everything(self):
        self.reg_frame.destroy()
        self.more_widgets_frame.destroy()
        