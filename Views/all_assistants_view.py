import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager
from tkinter import messagebox

class AllAssistantsView(ttk.Frame):

    def __init__(self, master, control, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "AllAssistantsView")

        self.control = control
        self.header = header

        self.view_name = "All Assistants"

    def populate_assistants(self):
        self.header.update_header(self.view_name)
        ViewManager.instance.show_view("AllAssistantsView")
        for widget in self.winfo_children():
            widget.destroy()

        self.all_assistants = self.control.get_assistants()

        ''' EDITING ASSISTANTS '''
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.assistant_info = ttk.Treeview(self)
        self.assistant_info['columns'] = ("f_name","l_name","pin","email","phone","role")
        self.assistant_info.column("#0", width=70)
        self.assistant_info.column("f_name",width=90)
        self.assistant_info.column("l_name",width=90)
        self.assistant_info.column("pin",width=40)
        self.assistant_info.column("email", width=120)
        self.assistant_info.column("phone",width=90)
        self.assistant_info.column("role",width=80)

        self.assistant_info.heading("#0",text="TeacherID")
        self.assistant_info.heading("f_name",text="FirstName")
        self.assistant_info.heading("l_name",text="LastName")
        self.assistant_info.heading("pin",text="PIN")
        self.assistant_info.heading("email",text="Email")
        self.assistant_info.heading("phone",text="Phone")
        self.assistant_info.heading("role",text="Role")

        self.assistant_info.grid(row=0, column=0, columnspan=2, sticky="NESW")
        self.assistant_info.bind('<ButtonRelease-1>', self.populate_teacher_info)

        for i in range (len(self.all_assistants)):
            # self.all_teachers[i][0] is the 'teacher_id' and the "values" are the rest of the teacher info.
            list_of_details = list(self.all_assistants[i])
            list_of_details[-1] = "Assistant"
            self.all_assistants[i] = tuple(list_of_details)
            self.assistant_info.insert("", tk.END, text=self.all_assistants[i][0], values=self.all_assistants[i][1:])

        ''' ASSISTANT DETAILS '''
        self.assistant_details = ttk.Labelframe(self, text="Teacher Details")
        self.assistant_details.grid(row=1, column=1)

        detail_names = ["First Name","Last Name","Pin","Email","Phone"]
        self.list_of_entries = []
        l_row = 1
        e_row = 2
        c = 1
        for i in range (len(detail_names)):
            if i == 3:
                l_row += 2
                e_row += 2
                c = 1
            detail_l = tk.Label(self.assistant_details, text=detail_names[i]).grid(row=l_row, column=c)
            self.detail_bx = tk.Entry(self.assistant_details, width=25)
            self.list_of_entries.append(self.detail_bx)
            self.detail_bx.grid(row=e_row, column=c)
            c += 1

        role_l = tk.Label(self.assistant_details, text="Role").grid(row=l_row,column=c)
        self.role_select = ttk.Combobox(self.assistant_details, textvariable=tk.StringVar())
        self.role_select['values'] = ("Manager","Teacher","Assistant")
        self.role_select.grid(row=e_row, column=c)

        ''' OTHER FUNCTIONS '''
        self.field_set = ttk.Labelframe(self, text="Functions")
        self.field_set.grid(row=1, column=0)
        
        ''' SAVING DETAILS '''
        self.save_btn = ttk.Button(self.field_set, text="SAVE", command= lambda: self.save_details())
        self.save_btn.grid(row=0, column=0, pady=5)

        ''' CLEARING DETAILS '''
        self.clear_btn = ttk.Button(self.field_set, text="CLEAR", command= lambda: self.clear_details())
        self.clear_btn.grid(row=1, column=0, pady=5)

        ''' ADDING ASSISTANT '''
        self.add_btn = ttk.Button(self.field_set, text="ADD", command= lambda: self.add_assistant())
        self.add_btn.grid(row=2, column=0, pady=5)
    
    def add_assistant(self): # validation here for format of all details!
        all_details = []
        for each_detail in self.list_of_entries:
            all_details.append(each_detail.get())
        self.control.add_staff(all_details[0], all_details[1], all_details[2], all_details[3], all_details[4], self.role_select.current())

    def save_details(self):
        all_details = []
        # Get index of selected teacher in treeview
        selected = self.assistant_info.focus()
        
        for each_detail in self.list_of_entries:
            all_details.append(each_detail.get())
        # Update treeview info
        self.assistant_info.item(selected, values=(all_details[0], all_details[1], all_details[2], all_details[3], all_details[4], self.role_select.get()))
        # Update DataBase
        self.control.update_staff_info(self.curr_assistant_id, all_details[0], all_details[1], all_details[2], all_details[3], all_details[4], self.role_select.current()) ## NOT FINSIHED YET!!!
        messagebox.showinfo("Save Complete!","Swimmer Info Updated!")

    def clear_details(self):
        for each_detail in self.list_of_entries:
            each_detail.delete(0, tk.END)
        self.role_select.set(value="")
        
    def populate_teacher_info(self, event=None):
        # clears contents of each entry widget before adding info
        for each_box in self.list_of_entries:
            each_box.delete(0, tk.END)

        item = self.assistant_info.selection()
        # 'item' contains the index of the items in the treeview. We can now reference specific info on the treeview.
        for i in item:
            curr_item = self.assistant_info.focus()
            item_dict = self.assistant_info.item(curr_item)

            all_info = self.assistant_info.item(i, "values")
            all_info = list(all_info)
            # the 'text' value in a treeview is my teacher_id
            self.curr_assistant_id = item_dict["text"]
            del all_info[-1] # remove the "Role" here as it's not needed.

        # populate entry widgets here 
        curr_entry = 0
        for each_info in all_info:
            self.list_of_entries[curr_entry].insert(0, each_info)
            curr_entry += 1
        self.role_select.set(value="Assistant")
        