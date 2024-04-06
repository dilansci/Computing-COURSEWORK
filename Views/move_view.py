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

    def moving_layout(self, swimmer_id, swimmer_name):
        self.header.update_header(self.view_name)

        ViewManager.instance.show_view("MoveView")
        for widget in self.winfo_children():
            widget.destroy()   

        self.swimmer_id = swimmer_id
        self.swimmer_name = swimmer_name

        # Get all classes
        self.class_ids = self.class_control.get_all_classes()
        ''' 
        TODOLIST
        * get all staff_ID with access_level 0 OR 1, level of class, Time, day USING CLASS_IDS
        * Create treeview (withing a scroll_widget) containing this info
        * Display swimmer name and current level ABOVE treeview
        * Make .bind on select for treeview which will make MOVE button active
        * On pressing MOVE button, make new 'move_class' service using swimmer_ID and the new class_ID selected
        * Put up confirmation messagebox displaying the change.
        * Exit view and go into 'AssessmentView' (OR go straight back to RegisterView, might be better!)
        
        '''
        self.teachers = 
