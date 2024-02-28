import SQL_controller

class ClassService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller

    # Already in regService
    # def get_classes(self): # this will get all classes, Probably gonna display class_info too :)) 
    #     return self.control.run_execute("SELECT * ")
    def get_all_teachers(self):
        return self.control.run_execute("SELECT first_name, last_name FROM Staff")
    
    def get_all_teachers_id(self):
        return self.control.run_execute("SELECT staff_ID FROM Staff")