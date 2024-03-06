import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager
from tkinter import messagebox

class EditSowView(ttk.Frame):

    def __init__(self, master, control, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "EditSowView")

        self.control = control
        self.header = header

        self.view_name = "Edit SOW"

    def edit_sow(self, data, listbox_label, sow_id): # label of listbox (to pass into update_sow()). */* UPDATE SOW SET {sow_label}=new_data */*
        self.header.update_header(self.view_name)

        ViewManager.instance.show_view("EditSowView")
        for widget in self.winfo_children():
            widget.destroy()

        self.data = data
        self.listbox_label = listbox_label
        self.sow_id = sow_id

        self.sow_contents = tk.Text(self, width=77)
        self.sow_contents.grid(sticky="NESW")
        self.sow_contents.insert(tk.END, self.data)

        self.save_btn = ttk.Button(self, text="SAVE", command= lambda: [self.save_sow(), ViewManager.instance.pop()]) # if we .pop() here, then Header displays wrong info!
        self.save_btn.grid()

    
    def save_sow(self): # use 'new_data' to pass into "update_sow(new_data)""
        new_data = self.sow_contents.get("1.0",END)

        self.control.update_class_sow(self.listbox_label, new_data, self.sow_id)
        messagebox.showinfo("Success!","SOW UPDATED!")