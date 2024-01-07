import SQL_controller

class LessonService():
    ## The 'sqlcontroller' will be a link to the database in SQL 
    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
    # need to think of service functions to use here. Will use alongside reg_controller :))