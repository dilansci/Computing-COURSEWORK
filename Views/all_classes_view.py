import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager
from tkinter import messagebox

class AllClassesView(ttk.Frame):

    def __init__(self, master, control, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "AllClassesView")

        self.class_control = control
        self.header = header
        self.view_name = "All Classes"

    def classes_layout(self):
        self.header.update_header(self.view_name)

        ViewManager.instance.show_view("AllClassesView")
        for widget in self.winfo_children():
            widget.destroy()
        

        ''' ALL CLASSES '''
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.column_names = ("teacher_id", "level", "time", "teacher","day")
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

        self.class_list.grid(row=0, column=0, columnspan=2, sticky="NESW")
        self.class_list.bind('<ButtonRelease-1>', self.select_class)


        ''' GETTING/INSERTING CLASSES '''
        self.class_ids = self.class_control.get_all_classes_ids()
        self.staff_ids = self.class_control.get_all_teachers_id()
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


        ''' OTHER FUNCTIONS '''
        self.field_set = ttk.Labelframe(self, text="Functions")
        self.field_set.grid(row=1, column=0)
        # SAVE
        self.save_btn = ttk.Button(self.field_set, text="SAVE", command= lambda: self.save_details())
        self.save_btn.grid(row=1, column=0, pady=5)
        # CLEAR
        self.clear_btn = ttk.Button(self.field_set, text="CLEAR", command= lambda: self.clear_details())
        self.clear_btn.grid(row=2, column=0, pady=5)
        # ADD CLASS
        self.add_btn = ttk.Button(self.field_set, text="ADD", command= lambda: self.add_class())
        self.add_btn.grid(row=3, column=0, pady=5)
        # REMOVE CLASS
        self.remove_btn = ttk.Button(self.field_set, text="REMOVE", command= lambda: self.remove_class())
        self.remove_btn.grid(row=4, column=0, pady=5)
        # self.remove_btn.config(state="disabled")


        ''' CLASS DETAILS '''
        self.class_details = ttk.Labelframe(self, text="Class Details")
        self.class_details.grid(row=1, column=1)

        self.staff_names = self.class_control.get_all_teachers()
        staff_names = []
        for each_name in self.staff_names:
            staff_names.append(f"{each_name[0]} {each_name[1]}")

        detail_names = ["Level", "Time", "TeacherID", "Day"]
        self.list_of_combos = []
        l_row = 1
        e_row = 2
        c = 1
        for i in range (len(detail_names)):
            if i == 3:
                l_row += 2
                e_row += 2
                c = 1
            detail_l = tk.Label(self.class_details, text=detail_names[i]).grid(row=l_row, column=c)
            self.combo_bx = ttk.Combobox(self.class_details, textvariable=tk.StringVar())
            self.list_of_combos.append(self.combo_bx)
            self.combo_bx.grid(row=e_row, column=c)
            c += 1
        # Levels
        self.list_of_combos[0]['values'] = (1,2,3,4,5,6,7)
        # Time
        self.list_of_combos[1]['values'] = ("5:00","5:30","6:00","6:30","7:00","7:30","8:00")
        # Teachers
        self.list_of_combos[2]['values'] = self.staff_ids
        # Day
        self.list_of_combos[3]['values'] = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")
        

    def select_class(self, event=None):
        # clears contents of each entry widget before adding info
        for each_box in self.list_of_combos:
            each_box.delete(0, tk.END)

        item = self.class_list.selection()
        # 'item' contains the index of the items in the treeview. We can now reference specific info on the treeview.
        for i in item:
            curr_item = self.class_list.focus()
            item_dict = self.class_list.item(curr_item)

            all_info = self.class_list.item(i, "values")
            all_info = list(all_info)
            # Rearranging Class data for displaying
            teacher_id = all_info[0]
            del all_info[0]
            del all_info[2]
            class_day = all_info[2]
            del all_info[2]
            all_info.append(teacher_id)
            all_info.append(class_day)

        curr_item = 0
        for each_item in all_info:
            self.list_of_combos[curr_item].set(value=each_item)
            curr_item += 1
    
    def save_details(self):
        all_details = []
        selected = self.class_list.focus()
        # Store class details in an array
        for each_box in self.list_of_combos:
            all_details.append(each_box.get())
         # Update treeview info
        class_id = self.class_list.item(selected, 'text')
        all_values = self.class_list.item(selected, 'values')
        teacher_name = all_values[3]
        self.class_list.item(selected, values=(all_details[2], all_details[0], all_details[1], teacher_name, all_details[3]))
        # Update database
        messagebox.showinfo("Confirmation","Successfully saved class!")
        self.class_control.update_class_info(class_id, all_details[0], all_details[1], all_details[2], all_details[3])
    
    def clear_details(self):
        for each_detail in self.list_of_combos:
            each_detail.set(value="")
        
    def add_class(self):
        class_details = []
        selected = self.class_list.focus()
        # Store class details in an array
        for each_box in self.list_of_combos:
            class_details.append(each_box.get())

        # Add class to database
        attempt = self.class_control.add_class(class_details[0], class_details[1], class_details[2], class_details[3])
        if attempt:
            messagebox.showinfo("Confirmation","Successfully added class!")
        else:
            messagebox.showerror("Error","This class already exists!")
        # Update treeview
        ViewManager.instance.refresh_pop()
        self.classes_layout()
        self.header.on_exit()
        self.clear_details()

    def remove_class(self):
        ''' slight kinks with remove_class'''
        selected = self.class_list.focus()
        # Remove class from database
        class_id = self.class_list.item(selected, 'text')
        self.class_control.remove_class(class_id)
        confirm = messagebox.askyesno("Confirmation","Are you sure you want to remove this class?")
        if confirm:
            messagebox.showinfo("Confirmation","Successfully removed class!")
        # Update treeview
        ViewManager.instance.refresh_pop()
        self.classes_layout()
        self.header.on_exit()
        self.clear_details()




