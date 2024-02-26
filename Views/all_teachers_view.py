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
        '''
        ______________
        OVERALL LAYOUT
        ______________
        Entry boxes will be made for each teacher in the DB.
        They will be split into "Mangers??", "Teachers" and "Assistants"
        Using a SQL query we will populate the box with the Teachers'/Assistants' FULLNAME followed by an "EDIT" button.
        _____________
        EDITING STAFF
        _____________
        On clicking the "EDIT" button it will open a new view "edit_staff" which contains all the info of the teacher.
        All of the states of the entry boxes will be enabled until "SAVE" is pressed, which will disable them all.
        SQL query will be run after this to UPDATE the info in each entrybox i.e. entry_box_name.get()
        ____________
        ADDING STAFF
        ____________
        An "ADD STAFF" button will be added to the "all_staff_view" frame.
        On click it will open a new view "add_staff" with a series of "Entry" widgets and "listboxes" (listbox for the access_level)
        After "SAVE" they will be brought back to the "edit_staff" view.


        '''
        self.all_teachers = self.control.get_teachers()
        self.fname_entries = []
        curr_id = 0
        r = 0
        for teacher in self.all_teachers:
            # This inserts the 'first_name' of each teacher into an entry box
            self.new_entry = ttk.Entry(self)
            self.new_entry.insert(0, teacher)
            self.new_entry.grid()
            self.new_entry.config(state="disabled")
            self.fname_entries.append(self.new_entry)
            # make an "edit" button which is linked to each 'new_entry'
            self.edit_btn = (ttk.Button(self, text="EDIT", command= lambda btn_id = curr_id: [ViewManager.instance.hide_view(self), self.edit_teacher.display_teacher_info(self.all_teachers, btn_id)])) # this command should bring to the edit_teacher view
            self.edit_btn.grid(row=r,column=1)
            r += 1
            curr_id += 1
            # self.edit_btn cmnd - "self.fname_entries[btn_id].config(state="active")"

        
