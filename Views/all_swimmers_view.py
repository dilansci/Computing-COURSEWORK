import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager
from tkinter import messagebox

class AllSwimmersView(ttk.Frame):

    def __init__(self, master, control, swimmer_edit, move_view, header, **kargs):
        super().__init__(master,**kargs)
        ViewManager.instance.register_view(self, "AllSwimmersView")
        ## USE DAY_CONTROLLER
        self.control = control
        self.header = header
        self.swimmer_edit = swimmer_edit
        self.move_view = move_view

        self.view_name = "All Swimmers"

    def populate_swimmers(self):
        self.header.update_header(self.view_name)
        
        ViewManager.instance.show_view("AllSwimmersView")
        for widget in self.winfo_children():
            widget.destroy()

        self.all_swimmers = self.control.get_swimmers()
        # removing 'Attendance' and 'passed' fields
        i = 0
        for each_info in self.all_swimmers:
            each_info = list(each_info)
            del each_info[6:]
            self.all_swimmers[i] = each_info
            i += 1

        ''' EDITING SWIMMERS '''
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.column_names = ("class_id","f_name","l_name","email","phone")
        self.swimmer_info = ttk.Treeview(self)
        self.swimmer_info['columns'] = self.column_names
        self.swimmer_info.column("#0", width=70)
        self.swimmer_info.column("class_id",width=50)
        self.swimmer_info.column("f_name",width=90)
        self.swimmer_info.column("l_name",width=90)
        self.swimmer_info.column("email", width=150)
        self.swimmer_info.column("phone",width=90)

        self.swimmer_info.heading("#0",text="SwimmerID")
        self.swimmer_info.heading("class_id",text="ClassID")
        self.swimmer_info.heading("f_name",text="FirstName")
        self.swimmer_info.heading("l_name",text="LastName")
        self.swimmer_info.heading("email",text="Email")
        self.swimmer_info.heading("phone",text="Phone")

        self.swimmer_info.grid(row=0, column=0, columnspan=2, sticky="NESW")
        self.swimmer_info.bind('<ButtonRelease-1>', self.populate_swimmer_info)

        for i in range (len(self.all_swimmers)):
            # self.all_swimmers[i][0] is the 'teacher_id' and the "values" are the rest of the teacher info.
            list_of_details = list(self.all_swimmers[i])
            self.all_swimmers[i] = tuple(list_of_details)
            self.swimmer_info.insert("", tk.END, text=self.all_swimmers[i][0], values=self.all_swimmers[i][1:])

        ''' SWIMMER DETAILS '''
        self.swimmer_details = ttk.Labelframe(self, text="Swimmer Details")
        self.swimmer_details.grid(row=1, column=1, sticky="W")

        # get rid of class_id from self.all_swimmers[i]
        detail_names = ["First Name","Last Name","Email","Phone"]
        self.list_of_entries = []
        l_row = 1
        e_row = 2
        c = 0
        for i in range (len(detail_names)):
            if i == 2:
                l_row += 2
                e_row += 2
                c = 0
            detail_l = tk.Label(self.swimmer_details, text=detail_names[i]).grid(row=l_row, column=c)
            self.detail_bx = tk.Entry(self.swimmer_details, width=25)
            self.list_of_entries.append(self.detail_bx)
            self.detail_bx.grid(row=e_row, column=c)
            c += 1
        
        self.send_content = ttk.Button(self.swimmer_details, text="S.E.N.D.", command= lambda: 
                                      [ViewManager.instance.hide_view(self), self.swimmer_edit.edit_layout(self.curr_swimmer_id,"SEND")]) # swimmer_id, field_name, SEND of swimmer
        self.send_content.grid(row=e_row+2, column=0, pady=5)
        self.send_content.config(state="disabled")
        # these 2 btns will take you to the same swimmer_edit view, passing parameters as either '''SEND or report'''
        self.report_content = ttk.Button(self.swimmer_details, text="REPORT", command= lambda: messagebox.showinfo("","Not implemented"))
        self.report_content.grid(row=e_row+2, column=1, pady=5)

        ''' OTHER FUNCTIONS '''
        self.field_set = ttk.Labelframe(self, text="Functions")
        self.field_set.grid(row=1, column=0, sticky="W")
        ''' SAVING DETAILS '''
        self.save_btn = ttk.Button(self.field_set, text="SAVE", command= lambda: self.save_details())
        self.save_btn.grid(row=1, column=0, pady=5)
        ''' CLEARING DETAILS '''
        self.clear_btn = ttk.Button(self.field_set, text="CLEAR", command= lambda: self.clear_details())
        self.clear_btn.grid(row=2, column=0, pady=5)
        ''' ADDING SWIMMER '''
        self.add_btn = ttk.Button(self.field_set, text="ADD", command= lambda: self.add_swimmer()) # pass teacher_id here
        self.add_btn.grid(row=3, column=0, pady=5)

    def add_swimmer(self):
        all_details = []
        for each_detail in self.list_of_entries:
            if each_detail.get() == "":
                return messagebox.showerror("Error","Null data input detected. Please enter a valid input!")
            else: 
                all_details.append(each_detail.get())
        self.control.add_swimmer(all_details[0], all_details[1], all_details[2], all_details[3])
        messagebox.showinfo("Success!","Swimmer successfully added!")
        # Getting the new swimmer's swimmer_ID
        self.new_swimmer_id = self.control.get_swimmer_id(all_details[0], all_details[1])[0]
        full_name = f"{all_details[0]} {all_details[1]}"
        ViewManager.instance.hide_view(self)
        self.move_view.moving_layout(self.new_swimmer_id, full_name, "No Level")
        # Update treeview
        # ViewManager.instance.refresh_pop()
        # self.populate_swimmers()
        # self.header.on_exit()
        # self.clear_details()

    def save_details(self):
        item = self.swimmer_info.selection()

        all_details = []
        # Get index of selected teacher in treeview
        selected = self.swimmer_info.focus()
        for each_detail in self.list_of_entries:
            if each_detail.get() == "":
                return messagebox.showerror("Error","Null data input detected. Please enter a valid input!")
            else: 
                all_details.append(each_detail.get())
        # Update DataBase
        self.control.update_swimmer_info(self.curr_swimmer_id, all_details[0], all_details[1], all_details[2], all_details[3])
        self.clear_details()
        messagebox.showinfo("Save Complete!","Teacher Info Updated!")
        # Update treeview info
        print(item)
        for i in item:
            curr_item = self.swimmer_info.focus()
            item_dict = self.swimmer_info.item(curr_item)
            all_info = self.swimmer_info.item(i, "values")
            self.curr_class_id = all_info[0]
        # self.curr_class_id = 
        self.swimmer_info.item(selected, values=(self.curr_class_id, all_details[0], all_details[1], all_details[2], all_details[3]))

    def clear_details(self):
        for each_detail in self.list_of_entries:
            each_detail.delete(0, tk.END)
        self.deselect_item()
        self.send_content.config(state="disabled")
        
    def populate_swimmer_info(self, event=None):
        self.send_content.config(state="active")
        # clears contents of each entry widget before adding info
        for each_box in self.list_of_entries:
            each_box.delete(0, tk.END)

        item = self.swimmer_info.selection()
        # 'item' contains the index of the items in the treeview. We can now reference specific info on the treeview.
        for i in item:
            curr_item = self.swimmer_info.focus()
            item_dict = self.swimmer_info.item(curr_item)

            all_info = self.swimmer_info.item(i, "values")
            all_info = list(all_info)
            # the 'text' value in a treeview is my swimmer_id
            self.curr_swimmer_id = item_dict["text"]
            # remove class_id from all_info
            del all_info[0]

        curr_entry = 0
        for each_info in all_info:
            self.list_of_entries[curr_entry].insert(0, each_info)
            curr_entry += 1

    def deselect_item(self):
        for i in self.swimmer_info.selection():
            self.swimmer_info.selection_remove(i)