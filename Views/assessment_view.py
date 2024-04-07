import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager
from tkinter import messagebox

class AssessmentView(ttk.Frame):

    def __init__(self, master, control, move_view, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "AssessmentView")

        self.control = control
        self.move_view = move_view
        self.header = header

        self.view_name = "Assessment"

    def assessment_layout(self, swimmer_id, class_id):
        self.header.update_header(self.view_name)

        ViewManager.instance.show_view("AssessmentView")
        for widget in self.winfo_children():
            widget.destroy()

        self.swimmer_id = swimmer_id
        self.class_id = class_id

        self.syllabus_frame = ttk.Labelframe(self, text="Syllabus")
        self.syllabus_frame.grid()

        self.swimmer = self.control.get_swimmer(self.swimmer_id)
        self.swimmer_level = self.control.get_swimmer_level(self.class_id)

        ''' SWIMMER DETAILS '''
        self.full_name = f"{self.swimmer[1]} {self.swimmer[2]}"
        self.swimmer_info = tk.Label(self, text=f"| {self.full_name} | Level {self.swimmer_level} |").grid(row=0, column=0, sticky="W")

        ''' ASSESSMENT DETAILS '''
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)

        self.column_names = ("passed")
        self.skill_list = ttk.Treeview(self)
        self.skill_list['columns'] = self.column_names
        self.skill_list.column("#0")
        self.skill_list.column("passed")

        self.skill_list.heading("#0", text="Skill")
        self.skill_list.heading("passed", text="Passed")

        self.skill_list.grid(row=1, column=0, sticky="NESW")
        self.skill_list.bind('<ButtonRelease-1>', self.update_button_states)

        # Use Level_num to get skills for that level
        self.all_skills = self.control.get_skills(self.swimmer_level)
        self.swimmer_mark = self.control.get_mark(self.swimmer_id)
        if self.swimmer_mark[0] == 0:
            self.mark = "FAIL"
        else:
            self.mark = "PASS"

        for i in range (len(self.all_skills)):
            self.skill_list.insert("", tk.END, text=self.all_skills[i], values=self.mark)
        
        ''' BUTTONS '''
        self.button_frame = ttk.Labelframe(self, text="Functions")
        self.button_frame.grid(row=2, column=0, columnspan=4, sticky="W")

        self.change_mark = ttk.Button(self.button_frame, text="CHANGE MARK", command= lambda: self.update_mark())
        self.change_mark.config(state="disabled")
        self.change_mark.grid(row=0, column=0, sticky="W", pady=5, padx=5)
        
        self.pass_swimmer = ttk.Button(self.button_frame, text="PASS", command= lambda: self.move_swimmer())
        self.pass_swimmer.config(state="disabled")
        self.pass_swimmer.grid(row=0, column=1, sticky="W", pady=5, padx=5)

        self.pass_all = ttk.Button(self.button_frame, text="PASS ALL", command= lambda: self.update_all_marks())
        self.pass_all.grid(row=0, column=4, sticky="NESW")

    def update_button_states(self, event=None):
        self.change_mark.config(state="active")
        self.pass_swimmer.config(state="active")

    
    def update_mark(self):
        selected = self.skill_list.focus()
        # Get the 'state' of the mark i.e. PASS or FAIL
        curr_item = (self.skill_list.item(selected, 'values'))[0]
        if curr_item == "FAIL":
            self.skill_list.item(selected, values="PASS")
        else:
            self.skill_list.item(selected, values="FAIL")
    
    def move_swimmer(self):
        all_marks = []
        # Check the 'state' of Passed.
        for item_id in self.skill_list.get_children():
            item_children = (self.skill_list.item(item_id, 'values'))[0]
            all_marks.append(item_children)
        if "FAIL" in all_marks:
            messagebox.showinfo("Invalid Request","Unable to move swimmer as they have not passed in ALL skills")
            return
        # If no "FAIL" in all_marks. Pass swimmer_ID into 'move_view'
        ViewManager.instance.hide_view(self)
        self.move_view.moving_layout(self.swimmer_id, self.full_name, self.swimmer_level)

    def update_all_marks(self):
        for item_id in self.skill_list.get_children():
            self.skill_list.item(item_id, values="PASS")
        self.pass_swimmer.config(state="active")