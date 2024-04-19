import tkinter as tk
from tkinter import ttk
from tkinter.constants import *
from Views.view_manager import ViewManager
from tkinter import messagebox

class SwimmerEdit(ttk.Frame):
    
    def __init__(self, master, control, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "SwimmerEdit")
        # use day control and make edit_send and edit_report service
        self.control = control
        self.header = header

    def edit_layout(self, swimmer_id, field_name):
        # The field_name is used to reference the respecetive field in Swimmers i.e. SEND or report
        name = field_name.capitalize()
        self.view_name = f"{name} Edit"
        self.header.update_header(self.view_name)
        
        ViewManager.instance.show_view("SwimmerEdit")
        for widget in self.winfo_children():
            widget.destroy()

        self.swimmer_id = swimmer_id

        self.swimmer_send = self.control.get_send(self.swimmer_id)

        self.edit_contents = tk.Text(self, width=77, highlightthickness=2)
        self.edit_contents.config(highlightbackground="gray")
        self.edit_contents.grid(sticky="NESW")
        self.edit_contents.insert(tk.END, self.swimmer_send)

        self.save_btn = ttk.Button(self, text="SAVE", command= lambda: [self.save_send(), ViewManager.instance.pop()])
        self.save_btn.grid()
    
    def save_send(self):
        new_data = self.edit_contents.get("1.0", END)
        if new_data == "":
            messagebox.showerror("Error","No input detected! Please enter a valid input!")
        else:
            self.control.update_send(self.swimmer_id, new_data)
            messagebox.showinfo("Success","SEND successfully updated!")