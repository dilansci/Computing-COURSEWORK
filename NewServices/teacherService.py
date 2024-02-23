import SQL_controller

class TeacherService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller

    def new_teacher(self): # pass in details for adding new teacher
        pass