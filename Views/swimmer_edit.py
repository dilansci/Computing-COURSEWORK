import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager

class SwimmerEdit(ttk.Frame):
    
    def __init__(self, master, control, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "SwimmerEdit")
        # use day control and make edit_send and edit_report service
        self.control = control
        self.header = header

        # change view_name in layout fnct
    def edit_layout(self, field_name, data):
        name = field_name.capitalize()
        self.view_name = f"{name} Edit"

        self.header.update_header(self.view_name)
        
        ViewManager.instance.show_view("SwimmerEdit")
        for widget in self.winfo_children():
            widget.destroy()
    
        self.edit_contents = tk.Text(self, width=77)
        self.edit_contents.grid(sticky="NESW")
        self.edit_contents.insert(tk.END, self.data)

        self.save_btn = ttk.Button(self, text="SAVE", command= lambda: [self.save_sow(), ViewManager.instance.pop()])
        self.save_btn.grid()