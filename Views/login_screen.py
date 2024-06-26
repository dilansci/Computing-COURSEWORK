import tkinter as tk
from tkinter import ttk
from Views.view_manager import ViewManager
from account_manager import *
from tkinter import messagebox
class LoginScreen(ttk.Frame):

    def __init__(self, master, control, day_view, header, **kargs):
        super().__init__(master, **kargs)
        ViewManager.instance.register_view(self, "LoginScreen")

        self.control = control
        self.day_view = day_view
        self.header = header
    
    def login_layout(self, access_level):

        ViewManager.instance.show_view("LoginScreen")
        for widget in self.winfo_children():
            widget.destroy()

        # Displaying Role in Header
        staff_names = ["Manager","Teacher","Assistant"]
        self.access_level = access_level
        self.view_name = f"{staff_names[self.access_level]} Login"
        self.header.update_header(self.view_name)

        self.pin_l = ttk.Label(self, text="")
        self.pin_box = ttk.Entry(self, show="*")
        self.pin_box.grid(row=4, column=1)
        self.rowconfigure(4, weight=1)
        self.pin_box.delete(0, tk.END)
        self.pin_box.config(state="disabled")

        # create the "num pad" here
        self.btn_names = ["0","1","2","3","4","5","6","7","8","CLR","9","ENTER"]
        for i in range (len(self.btn_names)):
            self.rowconfigure(i, weight=1)
            self.columnconfigure(i, weight=1)
            self.pin_button = tk.Button(self, width=15, height=5, text=self.btn_names[i], command= lambda btn_id=i: self.get_pin_fnct(self.btn_names[btn_id]))
            self.pin_button.grid(row=i//3, column=i%3)

    def get_pin_fnct(self,btn_id):
        if btn_id == "CLR":
            # the 'pin_box' is becoming "active" to allow a character to be input and then "disables" to prevent any other input
            self.pin_box.config(state="active")
            self.pin_box.delete(0, tk.END)
            self.pin_box.config(state="disabled")

        elif btn_id == "ENTER":
            self.teacher_info = AccountManager.login(self.pin_box.get(), self.access_level, self.control)
            if self.teacher_info != None:
                self.real_pin = self.teacher_info[0]
                self.teacher_name = self.teacher_info[1] + " " + self.teacher_info[2]
                # might also add a query for getting teacher name, Put teacher name at top side of screen.
                if self.real_pin == self.pin_box.get():
                    # clear 'pin_box before hiding the frame
                    self.pin_box.config(state="active")
                    self.pin_box.delete(0, tk.END)
                    self.pin_box.config(state="disabled")

                    ViewManager.instance.hide_view(self)

                    self.day_view.day_layout(self.access_level, self.teacher_name)
            else:
                messagebox.showerror("Error","Incorrect Password!")
                self.pin_box.config(state="active")
                self.pin_box.delete(0, tk.END)
                self.pin_box.config(state="disabled")

        elif len(self.pin_box.get()) != 4:
            self.pin_box.config(state="active")
            self.pin_box.insert(tk.END, btn_id)
            self.pin_box.config(state="disabled")
        else:
            messagebox.showinfo("Length Error","Max. 4 digits!")