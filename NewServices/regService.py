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
    
    def get_attendance(self, swimmer_names):
        attendance_data = []
        for i in range (len(swimmer_names)):
            curr_attendance = self.control.run_execute("SELECT attendance FROM Swimmers WHERE first_name=? AND last_name=?",swimmer_names[i][0], swimmer_names[i][1])
            attendance_data.append(curr_attendance[0][0])
        return attendance_data

    def set_attendance(self, swimmer_names, curr_attendance):
        if curr_attendance == 0:
            self.control.run_execute("UPDATE Swimmers SET attendance=1 WHERE first_name=? AND last_name=?",swimmer_names[0], swimmer_names[1])
        else:
            self.control.run_execute("UPDATE Swimmers SET attendance=0 WHERE first_name=? AND last_name=?",swimmer_names[0], swimmer_names[1])