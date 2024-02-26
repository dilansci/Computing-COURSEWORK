import SQL_controller

class ClassService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller

    def get_class(self): # this will get all classes, Probably gonna display class_info too :)) 
        pass