import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager
from tkinter import messagebox
# use staff_controller & staffService
class EditTeacherView(ttk.Frame):

    def __init__(self, master, staff_control, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "EditTeacherView")

        self.control = staff_control
    
    def display_teacher_info(self, teachers, teacher_id):
        ViewManager.instance.show_view("EditTeacherView")
        for widget in self.winfo_children():
            widget.destroy() 

        self.selected_teacher = teachers[teacher_id]
        # passing the teacher's fname and lname to get teacher's info
        self.curr_teacher_info = self.control.get_teacher_info(self.selected_teacher[0], self.selected_teacher[1])
        curr_access_level = self.control.get_access_level(self.selected_teacher[0], self.selected_teacher[1])
        teacher_details = ["First Name","Last Name", "Pin", "Email", "Phone no."]

        r = 0
        each_display_box = []
        for each_info in self.curr_teacher_info:
            self.display_l = tk.Label(self, text=teacher_details[r]).grid(row=r)
            self.display_info = tk.Entry(self, width=20)
            self.display_info.insert(0, each_info)
            self.display_info.grid(row=r, column=1)
            each_display_box.append(self.display_info)
            r += 1

        # ROLE selection
        curr_fname = each_display_box[0].get()
        curr_lname = each_display_box[1].get()

        self.role_l = tk.Label(self, text="Role").grid()
        self.role_selection = ttk.Combobox(self, textvariable=tk.StringVar()) # combobox
        self.role_selection['state'] = 'readonly'
        self.role_selection['values'] = ("Manager",
                                         "Teacher",
                                         "Assistant")
        self.roles = ["Manager","Teacher","Assistant"]
        self.role_selection.set(self.roles[curr_access_level])
        self.role_selection.grid(row=r, column=1)
        self.new_access_level = curr_access_level
        # Binding the ComboBox to 'role_changed' function
        self.role_selection.bind('<<ComboboxSelected>>', self.role_changed)


        ## refresh the 'all_teachers_view'. Might import 'exit_config' and tie it to 'save' so that it goes back to 'all_teachers_view'. (IDK)
        self.save_btn = ttk.Button(self, text="SAVE", command= lambda: [self.control.update_teacher_info(curr_fname, curr_lname, each_display_box[0].get(), each_display_box[1].get(), each_display_box[2].get(), each_display_box[3].get(), each_display_box[4].get(), self.new_access_level), messagebox.showinfo("Save Success","Info Saved!")])
        self.save_btn.grid()

    def role_changed(self, event=None):
        for role in range (len(self.roles)):
            if self.role_selection.get() == self.roles[role]:
                self.new_access_level = role
