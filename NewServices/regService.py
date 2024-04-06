import SQL_controller

class RegisterService():
    ## The 'sqlcontroller' will be a link to the database in SQL 
    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
        
    def get_class(self, class_id):
        return self.control.run_execute("SELECT * FROM Class WHERE class_ID=?",class_id)

    def get_teacher_name(self, teacher_id):
        return self.control.run_execute("SELECT first_name, last_name FROM Staff WHERE staff_ID=?",teacher_id)
    
    def get_teacher(self, teacher_id):
        return self.control.run_execute("SELECT * FROM Teachers WHERE staff_ID=?",teacher_id)
    
    def get_sow(self, sow_id):
        return self.control.run_execute("SELECT * FROM SOW WHERE sow_ID=?",sow_id)
    
    def get_attendance(self, class_id):
        return self.control.run_execute("SELECT attendance FROM Swimmers WHERE class_id=?", class_id)

    def set_attendance(self, swimmer_id, curr_attendance):
        if curr_attendance == 0:
            self.control.run_execute("UPDATE Swimmers SET attendance=1 WHERE swimmer_id=?",swimmer_id)
        else:
            self.control.run_execute("UPDATE Swimmers SET attendance=0 WHERE swimmer_id=?",swimmer_id)