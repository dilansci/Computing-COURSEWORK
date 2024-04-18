import tkinter as tk
from header_config import *
from exit_config import *
import SQL_controller

from Views.view_manager import ViewManager
# Service imports
from NewServices.dayService import *
from NewServices.regService import *
from NewServices.sowService import *
from NewServices.loginService import *
from NewServices.staffService import *
from NewServices.classService import *
# Controller imports
from Controllers.day_controller import *
from Controllers.reg_controller import *
from Controllers.sow_controller import *
from Controllers.login_controller import *
from Controllers.staff_controller import *
from Controllers.class_controller import *
# View imports
from Views.reg_view import RegisterView
from Views.day_view import DayView
from Views.sow_view import SOWView
from Views.login_view import LoginView
from Views.login_screen import LoginScreen
from Views.all_teachers_view import AllTeachersView
from Views.all_assistants_view import AllAssistantsView
from Views.staff_select_view import StaffSelectView
from Views.edit_class_view import ClassView
from Views.edit_sow_view import EditSowView
from Views.assessment_view import AssessmentView
from Views.move_view import MoveView
from Views.all_classes_view import AllClassesView
from Views.all_swimmers_view import AllSwimmersView
from Views.swimmer_edit import SwimmerEdit
# creating a class which acts as a dictionary for all the contents of the registry.
class Main(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("LMS - v1.0")
        self.geometry("660x550")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # SINGLETON
        view_manager = ViewManager()

        ## SQL_CONTROLLER
        self.sql_control = SQL_controller.SQLController()

        ## SERVICES
        self.day_service = DayService(self.sql_control)
        self.reg_service = RegisterService(self.sql_control)
        self.sow_service = SOWService(self.sql_control)
        self.login_service = LoginService(self.sql_control)
        self.staff_service = StaffService(self.sql_control)
        self.class_service = ClassService(self.sql_control)

        ## CONTROLLERS
        self.day_control = DayController(self.day_service, self.reg_service)
        self.reg_control = RegController(self.reg_service, self.day_service)
        self.sow_control = SOWController(self.sow_service, self.day_service, self.class_service)
        self.login_control = LoginController(self.login_service)
        self.staff_control = StaffController(self.staff_service)
        self.class_control = ClassController(self.class_service, self.reg_service, self.day_service, self.sow_service)

        self.container = tk.LabelFrame(self)
        self.container.columnconfigure(0, weight=1)
        self.container.grid(sticky="NESW", padx=5, pady=5)

        self.header = Header(self.container)
        self.header.grid(row=0, column=0, padx=5, pady=5, sticky="NEW")

        self.exit_button = Exit(self.container, self.header)
        self.exit_button.grid(row=4, column=0, sticky="ESW")

        ## VIEWS
        #  Only VIEWS should have 'self.container' as a parameter!
        self.all_classes_view = AllClassesView(self.container, self.class_control, self.header)
        self.move_view = MoveView(self.container, self.class_control, self.header)
        self.swimmer_edit = SwimmerEdit(self.container, self.day_control, self.header)
        self.all_swimmers_view = AllSwimmersView(self.container, self.day_control, self.swimmer_edit, self.move_view, self.header)
        self.assessment_view = AssessmentView(self.container, self.sow_control, self.move_view, self.header)
        self.edit_sow_view = EditSowView(self.container, self.class_control, self.header)
        self.edit_class_view = ClassView(self.container, self.class_control, self.edit_sow_view, self.header)
        self.all_assist_view = AllAssistantsView(self.container, self.staff_control, self.header)
        self.all_teachers_view = AllTeachersView(self.container, self.staff_control, self.header)
        self.staff_select_view = StaffSelectView(self.container, self.all_teachers_view, self.all_assist_view, self.header)
        self.sow_view = SOWView(self.container, self.sow_control, self.header)
        self.r_view = RegisterView(self.container, self.reg_control, self.assessment_view, self.header)
        self.d_view = DayView(self.container, self.day_control, self.r_view, self.sow_view, self.staff_select_view, self.edit_class_view, self.all_classes_view, self.all_swimmers_view, self.header)
        self.login_screen = LoginScreen(self.container, self.login_control, self.d_view, self.header)
        self.login_view = LoginView(self.container, self.login_control, self.login_screen, self.header)
        
        # The LoginView is registered as the first view.
        view_manager.register_view(self.login_view, "LoginView")
        view_manager.show_view("LoginView")

if __name__ == '__main__':
    main = Main()
    main.mainloop()