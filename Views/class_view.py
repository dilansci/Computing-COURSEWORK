import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager

class ClassView(ttk.Frame):

    def __init__(self, master, control, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "ClassView")
        self.control = control
        self.header = header

        self.view_name = "Classes"

    # use swimmerService like in "day_view"
    def show_classes(self, class_id, sow_id, teacher_id): # , day, time, level, curr_class_id
        self.header.update_header(self.view_name)

        ViewManager.instance.show_view("ClassView")
        for widget in self.winfo_children():
            widget.destroy()

        self.class_id = class_id
        self.sow_id = sow_id
        self.teacher_id = teacher_id # use this to make the first selection in the ComboBox the current teacher.

        self.all_teachers_id = self.control.get_all_teachers_id()
        self.all_teachers = self.control.get_all_teachers()
        self.all_names = []
        for i in range (len(self.all_teachers)):
            self.all_names.append(f"{self.all_teachers[i][0]} {self.all_teachers[i][1]}")

        self.teacher_dict = {}
        i = 0
        for teacher in self.all_names:
            self.teacher_dict.update({teacher: self.all_teachers_id[i][0]})
            i += 1

        self.curr_teacher_name = self.control.get_teacher_name(self.teacher_id)
        self.curr_fname = self.curr_teacher_name[0]
        self.curr_lname = self.curr_teacher_name[1]

        self.teacher_select = ttk.Combobox(self, textvariable=tk.StringVar())
        self.teacher_select['state'] = 'readonly'
        self.teacher_select['values'] = (self.all_names)
        self.teacher_select.set(self.curr_teacher_name)
        self.teacher_select.grid()

        self.teacher_select.bind('<<ComboboxSelected>>', self.teacher_changed)

    def teacher_changed(self, event=None):
        print("NEW TEACHER",self.teacher_select.get())
        print("NEW TEACHER ID",self.teacher_dict.get(self.teacher_select.get()))
        '''
        HERE WE USE A SLQ QUERY TO UPDATE THE DB FOR THE TEACHER OF THIS CLASS
        e.g.
<<<<<<< HEAD
        get_lesson = (SELECT )
        UPDATE Class
=======
        UPDATE Class SET staff_ID=?, time=?, level_num=? WHERE class_ID=?, {values}  

        To Update SOW:
        get_lesson = UPDATE SOW SET intro=?, main=?, contrast=?, depth=? WHERE sow_ID=?, {values}
        '''
>>>>>>> 9d8e7a4c1f110cb6dd66d898e6b71074bc576ffe

        Adding a class goes as follow:
        ------------------------------
        - CREATE the class in 'Classes' table. ASSIGN 'staff_ID', 'level' and 'time' for class.

        - ADD the 'new_class' into 'Lessons' table. ASSIGN 'sow_ID' and 'day' to Lesson.
        (IN ORDER TO GET 'sow_ID' you need to know the current 'week' and the 'level' for that week. FROM THAT YOU CAN FETCH THE 'SOW')
        
        Editing a class goes as follows:
        --------------------------------
        - Listbox for storing each Swimmer. On_Click of swimmer, make 'REMOVE' button state = "active".
          ADD button which will open either:
          1. A new view with new_swimmers_to_add
          2. Have a seperate listbox with swimmers not in the class.
          There will also be a seperate function that will "ADD NEW SWIMMER"
        '''
        

        