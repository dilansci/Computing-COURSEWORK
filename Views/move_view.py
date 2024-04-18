import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager
from tkinter import messagebox

class MoveView(ttk.Frame):

    def __init__(self, master, control, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "MoveView")

        self.class_control = control
        self.header = header

        self.view_name = "Moving"

    def moving_layout(self, swimmer_id, swimmer_name, level):
        self.header.update_header(self.view_name)

        ViewManager.instance.show_view("MoveView")
        for widget in self.winfo_children():
            widget.destroy()   

        self.swimmer_id = swimmer_id
        self.swimmer_name = swimmer_name
        self.level = level
        
        ''' SWIMMER DETAILS '''
        self.swimmer_info = tk.Label(self, text=f"| {self.swimmer_name} | Level {self.level} |").grid(row=0, column=0, sticky="W")

        ''' ALL CLASSES '''
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.column_names = ("teacher_id", "level", "time", "teacher", "day")
        self.class_list = ttk.Treeview(self)
        self.class_list['columns'] = self.column_names
        self.class_list.column("#0", width=30)
        self.class_list.column("teacher_id", width=30)
        self.class_list.column("level", width=30)
        self.class_list.column("time", width=30)
        self.class_list.column("teacher", width=70)
        self.class_list.column("day", width=30)

        self.class_list.heading("#0", text="ClassID")
        self.class_list.heading("teacher_id", text="TeacherID")
        self.class_list.heading("level", text="Level")
        self.class_list.heading("time", text="Time")
        self.class_list.heading("teacher", text="Teacher")
        self.class_list.heading("day", text="Day")


        self.class_list.grid(row=1, column=0, sticky="NESW")
        self.class_list.bind('<ButtonRelease-1>', self.select_class)

        ''' GETTING/INSERTING CLASSES '''
        self.class_ids = self.class_control.get_all_classes_ids() # IDK IF I NEED THIS??
        self.staff_names = self.class_control.get_all_teachers()

        self.classes = self.class_control.get_all_classes() # IMPORTATNE!!!

        self.full_names = []
        self.all_class_days = []
        for each_id in self.classes:
            # This gets the teacher's name depending on the staff_ID
            teacher_name = self.class_control.get_teacher_name(each_id[1])
            class_day = self.class_control.get_class_day(each_id[0])
            # Append the 'full_name' into an array
            self.full_names.append(f"{teacher_name[0]} {teacher_name[1]}")
            self.all_class_days.append(class_day)

        # Appending the Full Names into 'self.classes'
        curr_name = 0
        for each_name in self.full_names:
            self.classes[curr_name] = list(self.classes[curr_name])
            self.classes[curr_name].append(each_name)
            self.classes[curr_name] = tuple(self.classes[curr_name])
            curr_name += 1
        # Appending the Class Days into 'self.classes'
        curr_day = 0
        for each_day in self.all_class_days:
            self.classes[curr_day] = list(self.classes[curr_day])
            self.classes[curr_day].append(each_day)
            self.classes[curr_day] = tuple(self.classes[curr_day])
            curr_day += 1

        for i in range (len(self.classes)):
            self.class_list.insert("", tk.END, text=self.classes[i][0], values=self.classes[i][1:])
        
    def select_class(self, event=None):
        selected = self.class_list.focus()

        new_class_id = self.class_list.item(selected, 'text')
        curr_values = self.class_list.item(selected, 'values')
        new_level = curr_values[1]
        confirm = messagebox.askyesno("Level Confirmation", f"Do you want to move {self.swimmer_name} from Level {self.level} to Level {new_level}?")
        if confirm:
            self.class_control.update_swimmer_class_id(new_class_id, self.swimmer_id)
            messagebox.showinfo("Move Confirmation", "Swimmer successfully moved!")
            self.header.on_exit()
            ViewManager.instance.pop()
