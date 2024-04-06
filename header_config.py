import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager
# this class which eventually be able to change the header shown depending on what functionality is being used i.e
# if in register section it will display "Lesson Manager - Register".
class Header(ttk.Frame):
    # header is a labelframe
    # 'header' class will constantly update the location in which the user is accessing.
    def __init__(self, master, **kargs):
        super().__init__(master, **kargs)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.head_label = ttk.Label(self, text="Lesson Manager")
        self.head_label.grid(row=0, column=0, sticky="NS")
        self.head_list = []
        ''' REFRESH FUNCTION | NOT WORKING! '''
        # photo = tk.PhotoImage(file= r"C:\Users\Dylan Branda\OneDrive\Documents\School YR14\Computing\Computing-COURSEWORK\Refresh_icon.png")
        # photo_resize = photo.subsample(35,35)
        # self.refresh_btn = tk.Button(self, text="Refresh", command= lambda: ViewManager.instance.refresh_view())
        # self.refresh_btn.grid(row=0, column=1)

    def update_header(self, name):
        self.head_list.append(name)
        self.head_label["text"] = "Lesson Manager - " + name
    
    def on_exit(self):
        if len(self.head_list) > 1:
            self.head_list.pop()
            self.head_label["text"] = "Lesson Manager - " + self.head_list[-1]
        elif len(self.head_list) == 1:
            self.head_list.pop()
            self.head_label["text"] = "Lesson Manager"