import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager

class AllTeachersView(ttk.Frame):

    def __init__(self, master, control, edit_teacher_view, **kargs): # add additional parameters
        super().__init__(master,**kargs)
        ViewManager.instance.register_view(self, "AllTeachersView")

        self.control = control
        self.edit_teacher = edit_teacher_view
        '''
        This view will show entry widgets containing the info needed for a teacher
        e.g. Fname, Lname, Phone, Email, Pin etc
        Use SQL query to then UPDATE the DB with this info.
        NEED TO MAKE A FUNCTION FOR ADDING A TEACHER TO A CLASS!!! (same with adding a new class with swimmers) :)
        '''
    def populate_teachers(self):
        ViewManager.instance.show_view("AllTeachersView")
        for widget in self.winfo_children():
            widget.destroy()
            
        self.all_teachers = self.control.get_teachers()
        self.fname_entries = []
        curr_id = 0
        r = 0
        for teacher in self.all_teachers:
            # This inserts the 'full_name' of each teacher into an entry box
            self.new_entry = ttk.Entry(self)
            self.new_entry.insert(0, teacher)
            self.new_entry.grid()
            self.new_entry.config(state="disabled")
            self.fname_entries.append(self.new_entry)
            # make an "edit" button which is linked to each 'new_entry'
            self.edit_btn = (ttk.Button(self, text="EDIT", command= lambda btn_id = curr_id: 
                                        [ViewManager.instance.hide_view(self), self.edit_teacher.display_teacher_info(self.all_teachers, btn_id)]))
                                        # this command brings you to 'edit_teacher_view.py'
            self.edit_btn.grid(row=r,column=1)
            r += 1
            curr_id += 1
            # self.edit_btn cmnd - "self.fname_entries[btn_id].config(state="active")"

        
