import SQL_controller

class ClassService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller

    # Already in regService
    # def get_classes(self): # this will get all classes, Probably gonna display class_info too :)) 
    #     return self.control.run_execute("SELECT * ")