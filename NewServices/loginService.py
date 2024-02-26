import SQL_controller

'''
SQLcontroller syntax:
return self.control.run_execute(sql query))
'''
class LoginService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
    
    def get_login(self, pin, access_level):
        try:
            return self.control.run_execute("SELECT staff_pin, first_name, last_name FROM Staff WHERE staff_pin=? AND access_level=?", pin, access_level)[0]
        except:
            return None