import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager
from Widgets.scroll_widgets import VerticalScrolledFrame
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
    def show_classes(self, class_id, sow_id, teacher_id, level):
        self.header.update_header(self.view_name)

        ViewManager.instance.show_view("ClassView")
        for widget in self.winfo_children():
            widget.destroy()

        self.edit_frame = VerticalScrolledFrame(self)
        self.edit_frame.grid(columnspan=7, sticky="NESW")
        # self.edit_frame.interior

        self.class_id = class_id
        self.sow_id = sow_id
        self.teacher_id = teacher_id
        self.curr_level = level

        ''' EDITING SOW '''
        self.sow_info = self.control.get_sow(sow_id)
        c = 0
        w = 30
        self.column_names = ("Intro", "Main", "Contrast", "Depth") 
        for i in range (0, len(self.column_names)):
             self.column_l = tk.Label(self.edit_frame.interior, text=self.column_names[i]).grid(row=0, column=i)
        # length check for each SOW
        truncated_infos = []
        self.list_of_listboxes = []
        for sow in range (len(self.sow_info)):
            info = self.sow_info[sow]
            if len(self.sow_info[sow]) > 35:
                info = info[0:35] + "..." + info[35:-1]
            truncated_infos.append(info)
            # adjusts the width for the 'depth' listbox
            if sow == 3:
                w = 10
            self.listbox = tk.Listbox(self.edit_frame.interior, width=w)
            self.listbox.insert(tk.END, truncated_infos[sow])
            self.listbox.grid(row=1, column=c)
            self.listbox.bind("<<ListboxSelect>>", self.edit_box)
            self.list_of_listboxes.append(self.listbox)
            c += 1

        ''' CHANGING TEACHER '''
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

        teacher_l = tk.Label(self, text="Teachers").grid(row=5, column=0)
        self.teacher_select = ttk.Combobox(self, textvariable=tk.StringVar())
        self.teacher_select['state'] = 'readonly'
        self.teacher_select['values'] = (self.all_names)
        self.teacher_select.set(self.curr_teacher_name)
        self.teacher_select.grid(row=6, column=0)

        self.teacher_select.bind('<<ComboboxSelected>>', self.teacher_changed)

        ''' CHANGING LEVEL '''
        level_l = tk.Label(self, text="Levels").grid(row=5, column=1)
        self.all_levels = [1,2,3,4,5,6,7]
        self.level_select = ttk.Combobox(self, textvariable=tk.StringVar())
        self.level_select['state'] = 'readonly'
        self.level_select['values'] = (self.all_levels)
        self.level_select.set(self.curr_level)
        self.level_select.grid(row=6, column=1)

        self.level_select.bind('<<ComboboxSelected>>', self.level_changed)

        ''' EDITING SWIMMERS '''
        self.swimmer_info = ttk.Treeview(self.edit_frame.interior)
        self.swimmer_info['columns'] = ("swimmer_id","f_name","l_name","email","phone")
        self.swimmer_info.column("#0", width=50)
        self.swimmer_info.column("swimmer_id", width=70)
        self.swimmer_info.column("f_name",width=100)
        self.swimmer_info.column("l_name",width=100)
        self.swimmer_info.column("email")
        self.swimmer_info.column("phone",width=100)

        self.swimmer_info.heading("#0",text="ClassID")
        self.swimmer_info.heading("swimmer_id", text="SwimmerID")
        self.swimmer_info.heading("f_name",text="FirstName")
        self.swimmer_info.heading("l_name",text="LastName")
        self.swimmer_info.heading("email",text="Email")
        self.swimmer_info.heading("phone",text="Phone")

        self.swimmer_info.grid(columnspan=8)
        self.swimmer_info.bind('<ButtonRelease-1>', self.populate_swimmer_info)
        # gets swimmers with the same class_id as the selected class
        self.all_swimmers = self.control.get_swimmers_from_class(self.class_id)
        print("ALL SDWIMMRES",self.all_swimmers)

        for i in range (len(self.all_swimmers)):
            # self.all_swimmers[i][0] is the 'class_id' and the "values" are the rest of the swimmer info.
            self.swimmer_info.insert("", tk.END, text=self.all_swimmers[i][0], values=self.all_swimmers[i][1:])

        ''' SWIMMER DETAILS '''
        detail_names = ["First Name","Last Name","Email","Phone"]
        self.list_of_entries = []
        for i in range (len(detail_names)):
            detail_l = tk.Label(self, text=detail_names[i]).grid(row=3, column=i)
            self.detail_bx = tk.Entry(self, width=25)
            self.list_of_entries.append(self.detail_bx)
            self.detail_bx.grid(row=4, column=i)
         
        ''' SAVING DETAILS '''
        self.save_btn = ttk.Button(self, text="SAVE", command= lambda: self.save_details())
        self.save_btn.grid(row=7, pady=10)
    
    def save_details(self):
        all_details = []
        for each_detail in self.list_of_entries:
            all_details.append(each_detail.get())
        self.control.update_swimmer_info(self.curr_swimmer_id, all_details[0], all_details[1], all_details[2], all_details[3])
        messagebox.showinfo("Save Complete!","Swimmer Info Updated!")

    def populate_swimmer_info(self, event=None):
        class_ids = self.control.get_all_classes()
        # clears contents of each entry widget before adding info
        for each_box in self.list_of_entries:
            each_box.delete(0, tk.END)

        item = self.swimmer_info.selection()
        # 'item' contains the index of the items in the treeview. We can now reference specific info on the treeview.
        for i in item:
            all_info = self.swimmer_info.item(i, "values")
            all_info = list(all_info)
            self.curr_swimmer_id = all_info[0]
            print(self.curr_swimmer_id)
            print("SLECTED",all_info)
            # removing the 'swimmer_id' and storing it as 'curr_swimmer_id'
            del all_info[0]

        # populate entry widgets here 
        curr_entry = 0
        for each_info in all_info:
            self.list_of_entries[curr_entry].insert(0, each_info)
            curr_entry += 1

    def edit_box(self, event):
        ViewManager.instance.hide_view(self)
        list_of_indexes = []
        if event.widget in self.list_of_listboxes:
            index = self.list_of_listboxes.index(event.widget)
            list_of_indexes.append(index)
        listbox_label = self.column_names[index].lower()

        selection = event.widget.curselection()
        if selection:
            # declaring the index for the listbox to access
            index = selection[0]
            data = (event.widget.get(index)).replace("...","")
            self.edit_sow_view.edit_sow(data, listbox_label, self.sow_id)

    def teacher_changed(self, event=None):
        new_teacher = self.teacher_select.get()
        new_teacher_id = self.teacher_dict.get(new_teacher)
        self.control.update_class_teacher(new_teacher_id, self.class_id)
        messagebox.showinfo("UPDATED INFO!",f"Updated teacher to '{new_teacher}'.")
    
    def level_changed(self, event=None):
        new_level = self.level_select.get()
        self.control.update_class_level(new_level, self.class_id)
        messagebox.showinfo("UPDATED INFO!",f"Updated Level to '{new_level}'.")

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