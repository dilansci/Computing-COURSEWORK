import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager
from tkinter import messagebox

class ClassView(ttk.Frame):

    def __init__(self, master, control, edit_sow_view, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "ClassView")
        self.control = control
        self.header = header
        self.edit_sow_view = edit_sow_view

        self.view_name = "Classes"

    # use swimmerService like in "day_view"
    def show_classes(self, class_id, sow_id, teacher_id): # , day, time, level, curr_class_id
        self.header.update_header(self.view_name)

        ViewManager.instance.show_view("ClassView")
        for widget in self.winfo_children():
            widget.destroy()

        self.class_id = class_id
        self.sow_id = sow_id
        self.teacher_id = teacher_id
        ## Editing SOW
        self.sow_info = self.control.get_sow(sow_id)

        c = 0
        w = 30
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
            # adjusts the width for the 'depth' listbox
            if sow == 3:
                w = 10
            self.listbox = tk.Listbox(self, width= w)
            self.listbox.insert(tk.END, truncated_infos[sow])
            self.listbox.grid(row=1, column=c)
            self.listbox.bind("<<ListboxSelect>>", self.edit_box)
            c += 1

        ## Changing Teacher
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

    def edit_box(self, event): # maybe pass in 'Label name' and 'sow_id'??
        ViewManager.instance.hide_view(self)
        # This is the ListBox object ' event.widget()
        # print("Listbox contents", event.widget.get(0))

        # selects the listbox widget
        selection = event.widget.curselection()
        if selection:
            # declaring the index for the listbox to access
            index = selection[0]
            data = (event.widget.get(index)).replace("...","")
            self.edit_sow_view.edit_sow(data)
        ## Might create a seperate view which displays the current 'selected' ListBox as a 'Text' widget.
        # test_text = tk.Text(self) ** THIS IS AN INTERACTIBLE TEXT WIDGET i.e. (You can type in here!) **


    def teacher_changed(self, event=None):
        new_teacher = self.teacher_select.get()
        new_teacher_id = self.teacher_dict.get(new_teacher)
        self.control.update_class(new_teacher_id, self.class_id)
        messagebox.showinfo("UPDATED INFO!",f"Updated teacher to {new_teacher}.")
        # print("NEW TEACHER",self.teacher_select.get())
        # print("NEW TEACHER ID",self.teacher_dict.get(self.teacher_select.get()))
        '''
        HERE WE USE A SLQ QUERY TO UPDATE THE DB FOR THE TEACHER OF THIS CLASS
        e.g.
        UPDATE Class SET staff_ID=?, time=?, level_num=? WHERE class_ID=?, {values}  

        To Update SOW:
        get_lesson = UPDATE SOW SET intro=?, main=?, contrast=?, depth=? WHERE sow_ID=?, {values}


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