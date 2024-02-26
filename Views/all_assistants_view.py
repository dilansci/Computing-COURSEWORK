import tkinter as tk
from tkinter import ttk
from tkinter.constants import * 
from Views.view_manager import ViewManager


class AllAssistantsView(ttk.Frame):

    def __init__(self, master, control, edit_assistant_view, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "AllAssistantsView")

        self.control = control
        self.edit_assistant= edit_assistant_view

    def populate_assistants(self):
        ViewManager.instance.show_view("AllAssistantsView")
        for widget in self.winfo_children():
            widget.destroy()

        self.all_assistants = self.control.get_assistants()
        self.fname_entries = []
        curr_id = 0
        r = 0
        for assist in self.all_assistants:
            # This inserts the 'first_name' of each teacher into an entry box
            self.new_entry = ttk.Entry(self)
            self.new_entry.insert(0, assist)
            self.new_entry.grid()
            self.new_entry.config(state="disabled")
            self.fname_entries.append(self.new_entry)
            # make an "edit" button which is linked to each 'new_entry'
            self.edit_btn = (ttk.Button(self, text="EDIT", command= lambda btn_id = curr_id: [ViewManager.instance.hide_view(self), self.edit_assistant.display_assist_info(self.all_assistants, btn_id)])) # this command should bring to the edit_teacher view
            self.edit_btn.grid(row=r,column=1)
            r += 1
            curr_id += 1
        