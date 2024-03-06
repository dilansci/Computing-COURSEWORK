import SQL_controller

class ClassService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller

    def get_all_teachers(self):
        return self.control.run_execute("SELECT first_name, last_name FROM Staff")
    
    def get_all_teachers_id(self):
        return self.control.run_execute("SELECT staff_ID FROM Staff")
    
    def update_class_teacher(self, teacher_id, class_id):
        return self.control.run_execute("UPDATE Class SET staff_ID=? WHERE class_ID=?",teacher_id, class_id)

    def update_class_level(self, new_level, class_id):
        return self.control.run_execute("UPDATE Class SET level_num=? WHERE class_ID=?",new_level, class_id)
    
    def update_class_sow(self, sow_label, new_data, sow_id):
        print("IN SERVICE! NAME:",sow_label)
        return self.control.run_execute(f"UPDATE SOW SET {sow_label}=? WHERE sow_ID=?",new_data.strip(), sow_id)