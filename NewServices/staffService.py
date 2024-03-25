import SQL_controller

class StaffService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller

    def new_teacher(self): # pass in details for adding new teacher
        pass

    def get_teachers(self):
        return self.control.run_execute("SELECT first_name, last_name FROM Staff WHERE access_level=1")
    
    def get_assistants(self):
        return self.control.run_execute("SELECT first_name, last_name FROM Staff WHERE access_level=2")
    
    def get_teacher_info(self, fname, lname):
        return self.control.run_execute("SELECT first_name, last_name, staff_pin, email, phone FROM Staff WHERE first_name=? AND last_name=?",fname, lname)[0]
    
    def get_access_level(self, fname, lname):
        return self.control.run_execute("SELECT access_level FROM Staff WHERE first_name=? AND last_name=?",fname, lname)[0][0]
    
    def update_teacher_info(self, old_fname, old_lname, fname, lname, pin, email, phone, access_level):
        return self.control.run_execute("UPDATE Staff SET first_name=?, last_name=?, staff_pin=?, email=?, phone=?, access_level=? WHERE first_name=? AND last_name=?"
                                        ,fname, lname, pin, email, phone, access_level, old_fname, old_lname)