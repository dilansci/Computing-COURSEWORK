import SQL_controller

class RegisterService():
    ## The 'sqlcontroller' will be a link to the database in SQL 
    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
    
    def get_class(self, class_id):
        return self.control.run_execute("SELECT * FROM Class WHERE class_ID=?",class_id)
    
    def get_teacher_name(self, teacher_id):
        return self.control.run_execute("SELECT first_name, surname FROM Teachers WHERE teacher_ID=?",teacher_id)
    
    def get_teacher(self, teacher_id):
        return self.control.run_execute("SELECT * FROM Teachers WHERE teacher_ID=?",teacher_id)
    
    def get_sow(self, sow_id):
        return self.control.run_execute("SELECT * FROM SOW WHERE sow_ID=?",sow_id)
    
    def get_attendance(self, swimmer_names):
        data = []
        for i in range (len(swimmer_names)):
            curr_attendance = self.control.run_execute("SELECT attendance FROM Swimmers WHERE first_name=? AND last_name=?",swimmer_names[i][0], swimmer_names[i][1])
            data.append(curr_attendance[0][0])
        
        return data

    def set_attendance(self, swimmer_names, data):
        for each_name in range (len(swimmer_names)):
            if data[each_name] == 0:
                self.control.run_execute("UPDATE Swimmers SET attendance=1 WHERE first_name=? AND last_name=?",swimmer_names[each_name][0], swimmer_names[each_name][1])
            else:
                self.control.run_execute("UPDATE Swimmers SET attendance=0 WHERE first_name=? AND last_name=?",swimmer_names[each_name][0], swimmer_names[each_name][1])