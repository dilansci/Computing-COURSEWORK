import tkinter as tk
from header_config import *
from exit_config import *
from register import *
import SQL_controller

from Views.view_manager import ViewManager
# Service imports
from NewServices.swimmerService import *
from NewServices.regService import *
from NewServices.syllabusService import *
# Controller imports
from Controllers.day_controller import *
from Controllers.reg_controller import *
from Controllers.sow_controller import *
# View imports
from Views.reg_view import RegisterView
from Views.day_view import DayView
from Views.sow_view import SOWView

# creating a class which acts as a dictionary for all the contents of the registry.
class Main(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("SwimmerDB")
        self.geometry("650x500")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # most of the code/widgets will be stored with the 'self.container' frame.
        self.container = tk.LabelFrame(self)
        # specifiying the area where the 'container' frame is packed within 'Main'.
        self.container.columnconfigure(0, weight=1)
        self.container.grid(sticky="NESW", padx=5, pady=5)

        self.header = Header(self.container)
        self.header.grid(row=0, column=0, padx=5, pady=5, sticky="NEW")
        # where the 'BACK' button is instanciated
        self.exit_button = Exit(self.container)
        self.exit_button.grid(row=4, column=0, sticky="ESW")

        # SINGLETON
        # Establishing the first Singleton connection as 'DayView' (will change to login at some point)
        view_manager = ViewManager()

        ## SQL_CONTROLLER
        self.sql_control = SQL_controller.SQLController()

        ## SERVICES
        self.day_service = SwimmerService(self.sql_control)
        self.reg_service = RegisterService(self.sql_control)
        self.sow_service = SOWService(self.sql_control)

        ## CONTROLLERS
        self.day_control = DayController(self.day_service, self.reg_service)
        self.reg_control = RegController(self.reg_service, self.day_service)
        self.sow_control = SOWController(self.sow_service)

        ## VIEWS
        #  Only VIEWS should have 'self.container' as a parameter!
        self.sow_view = SOWView(self.container, self.sow_control)
        self.r_view = RegisterView(self.container, self.reg_control)
        self.d_view = DayView(self.container, self.day_control, self.r_view, self.sow_view)

        view_manager.register_view(self.d_view, "DayView")
        view_manager.show_view("DayView")

'''
Need to instanciate all the controllers and services inside of main!
A controller needs to be passed into a view and there should only exist 1 of each controller/service.

SQLController goes into Service, Service goes into respective Controller, Controller goes into View.
*** These are all created in main!!! ***
'''


if __name__ == '__main__':
    main = Main()
    main.mainloop()