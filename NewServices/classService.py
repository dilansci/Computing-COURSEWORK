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
    
    def update_class(self, teacher_id, class_id):
        print("TEACHER ID",teacher_id, "CLASS ID",class_id)
        return ("UPDATE Class SET staff_ID=? WHERE class_ID=?",teacher_id, class_id)
