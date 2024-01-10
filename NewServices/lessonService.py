import SQL_controller

class LessonService():
    ## The 'sqlcontroller' will be a link to the database in SQL 
    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
    
    def get_class(self, class_id): # use class_ID as parameter here :))
        return self.control.run_execute("SELECT * FROM Class WHERE class_ID=?",class_id)
    
    def get_teacher_name(self, teacher_id): # might want to change this to 'get_teacher_info' to prevent creating multiple services.
        return self.control.run_execute("SELECT first_name, surname FROM Teachers WHERE teacher_ID=?",teacher_id)
    
    def get_teacher(self, teacher_id):
        return self.control.run_execute("SELECT * FROM Teachers WHERE teacher_ID=?",teacher_id)