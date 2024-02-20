import SQL_controller

class LoginService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
    
    def get_login(self): #pass through entered login from entry widget
        pass