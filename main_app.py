import tkinter as tk
from tkinter import ttk
from header_config import *
from register import *

import SQL_controller
# Service imports
from NewServices.swimmerService import *
from NewServices.lessonService import *
# Controller imports
from Controllers.day_controller import *
from Controllers.reg_controller import *
# View imports
from Views.day_view import DayView
from Views.reg_view import RegisterView

class Main(tk.Tk):

    # creating a class which acts as a dictionary for all the contents of the registry.
    def __init__(self):
        super().__init__()
        self.title("SwimmerDB")
        self.geometry("600x500")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # most of the code/widgets will be stored with the 'self.container' frame.
        self.container = tk.LabelFrame(self)
        # specifiying the area where the 'container' frame is packed within 'Main'.
        self.container.columnconfigure(0, weight=1)
        self.container.grid(sticky="NESW", padx=5, pady=5)
        # this is the frame where the header from 'header_config' will be displayed.
        self.header = Header(self.container)
        self.header.grid(row=0, column=0, padx=5, pady=5, sticky="NEW")

        ## SQL_CONTROLLER
        self.sql_control = SQL_controller.SQLController()
        info = SQL_controller.SQLController().run_execute("SELECT * FROM Lessons WHERE day=?","Monday")
        print("ALl my info",info)
        ## SERVICES

        self.day_service = SwimmerService(self.sql_control)
        self.reg_service = LessonService(self.sql_control)

        ## CONTROLLERS
        self.day_control = DayController(self.day_service)
        self.reg_control = RegController(self.reg_service)


        ## VIEWS
        # *** Only VIEWS should have 'self.container' as a parameter! ***
        self.d_view = DayView(self.container, self.day_control)
        self.d_view.grid(row=1, column=0, padx=5, pady=5)

        self.r_view = RegisterView(self.container, "Monday", self.reg_control) # When day = "Monday" it sets Monday as the default register to open.
        self.r_view.grid(row=2, column=0, padx=5, pady=5) # did a good :)

'''
Need to instanciate all the controllers and services inside of main!
A controller needs to be passed into a view and there should only exist 1 of each controller/service.

SQLController goes into Service, Service goes into respective Controller, Controller goes into View.
*** These are all created in main!!! ***
'''


if __name__ == '__main__':
    main = Main()
    main.mainloop()