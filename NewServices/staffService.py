import SQL_controller

class StaffService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller

    def new_teacher(self): # pass in details for adding new teacher
        pass

    def get_teachers(self):
        print("I AM IN STAFF SERVICE")
        return self.control.run_execute("SELECT first_name, last_name FROM Staff WHERE access_level=1")
    
    def get_assistants(self):
        return self.control.run_execute("SELECT first_name, last_name FROM Staff WHERE access_level=2")