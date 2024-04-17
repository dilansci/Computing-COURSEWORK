import SQL_controller

class DayService():
    
    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller

    def get_swimmers(self):
        return self.control.run_execute("SELECT * FROM Swimmers")
    
    def get_lessons_day(self, day):
        return self.control.run_execute("SELECT * FROM Lessons WHERE day=?", day)

    def get_swimmer_name(self, class_id):
        return self.control.run_execute("SELECT first_name, last_name FROM Swimmers WHERE class_ID =?", class_id)

    def add_swimmer(self, f_name, l_name, email, phone):
        return self.control.run_execute(f"INSERT INTO Swimmers (first_name, last_name, email, phone) VALUES ('{f_name}','{l_name}','{email}','{phone}')")
    
    def get_swimmers_in_class(self, class_id):
        return self.control.run_execute("SELECT swimmer_ID, first_name, last_name FROM Swimmers WHERE class_ID=?", class_id)
    
    def get_swimmer(self, swimmer_id):
        return self.control.run_execute("SELECT swimmer_ID, first_name, last_name FROM Swimmers WHERE swimmer_ID=?", swimmer_id)
    
    def get_mark(self, swimmer_id):
        return self.control.run_execute("SELECT passed FROM Swimmers WHERE swimmer_ID=?", swimmer_id)[0]
    
    def get_send(self, swimmer_id):
        return self.control.run_execute("SELECT SEND FROM Swimmers WHERE swimmer_ID=?", swimmer_id)
    
    def update_send(self, swimmer_id, send):
        return self.control.run_execute("UPDATE Swimmers SET SEND=? WHERE swimmer_ID=?",send, swimmer_id)

    def update_swimmer_info(self, swimmer_id, f_name, l_name, email, phone):
        return self.control.run_execute("UPDATE Swimmers SET first_name=?, last_name=?, email=?, phone=? WHERE swimmer_ID=?", 
                                        f_name, l_name, email, phone, swimmer_id)
    