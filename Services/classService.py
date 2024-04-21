import SQL_controller

class ClassService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller

    def get_all_classes_ids(self):
        return self.control.run_execute("SELECT class_ID FROM Class")
    
    def get_all_teachers(self):
        return self.control.run_execute("SELECT first_name, last_name FROM Staff")
        
    def get_all_teachers_id(self):
        return self.control.run_execute("SELECT staff_ID FROM Staff")
    
    def get_class_day(self, class_id):
        return self.control.run_execute("SELECT day FROM Lessons WHERE class_ID=?", class_id)

    def get_all_classes(self):
        return self.control.run_execute("SELECT * FROM Class")
    
    def get_swimmers_from_class(self, class_id):
        return self.control.run_execute("SELECT class_ID, swimmer_ID, first_name, last_name, email, phone FROM Swimmers WHERE class_ID=?",class_id)
    
    def get_swimmer_level(self, class_id):
        return self.control.run_execute("SELECT level_num FROM Class WHERE class_id=?", class_id)[0][0]

    def update_class_teacher(self, teacher_id, class_id):
        return self.control.run_execute("UPDATE Class SET staff_ID=? WHERE class_ID=?",teacher_id, class_id)

    def update_class_level(self, new_level, class_id):
        self.control.run_execute("UPDATE Class SET level_num=? WHERE class_ID=?",new_level, class_id)
        return self.control.run_execute("UPDATE Lessons SET sow_ID=? WHERE class_ID=?", new_level, class_id)
    
    def update_class_sow(self, sow_label, new_data, sow_id):
        new_data.strip()
        return self.control.run_execute(f"UPDATE SOW SET {sow_label}=? WHERE sow_ID=?",new_data, sow_id)
    
    def update_swimmer_info(self, swimmer_id, f_name, l_name, email, phone):
        return self.control.run_execute(f"UPDATE Swimmers SET first_name=?, last_name=?, email=?, phone=? WHERE swimmer_ID={swimmer_id}",f_name, l_name, email, phone)
    
    def update_swimmer_class_id(self, class_id, swimmer_id):
        return self.control.run_execute("UPDATE Swimmers SET class_ID=? WHERE swimmer_ID=?", class_id, swimmer_id)

    def update_class_info(self, class_id, level, time, teacher_id, day):
        update_class = self.control.run_execute("UPDATE Class SET staff_ID=?, level_num=?, time=? WHERE class_ID=?", teacher_id, level, time, class_id)
        update_class_day = self.control.run_execute("UPDATE Lessons SET Day=? WHERE class_ID=?", day, class_id)
        return update_class, update_class_day
    
    def add_class(self, level, time, teacher_id, day):
        self.control.run_execute(f"INSERT INTO Class (staff_ID, level_num, time) VALUES ('{teacher_id}','{level}', '{time}')")
        new_class_id = self.control.run_execute("SELECT class_ID FROM Class WHERE staff_ID=? AND level_num=? AND time=?", teacher_id, level, time)

        if (len(new_class_id)) > 1:
            for invalid_id in (new_class_id[1:]):
                print(invalid_id[0])
                self.control.run_execute(f"DELETE FROM Class WHERE class_ID=?",invalid_id[0])
            # 'False' means it's invalid
            return False
        else:
            new_class_id = new_class_id[0][0]
            self.control.run_execute(f"INSERT INTO Lessons (class_ID, sow_ID, day) VALUES ('{new_class_id}', '{level}', '{day}')")
            # 'True' means it's valid
            return True
    
    def remove_class(self, class_id):
        self.control.run_execute("DELETE FROM Class WHERE class_ID=?", class_id)
        self.control.run_execute("DELETE FROM Lessons WHERE class_ID=?", class_id)
    
