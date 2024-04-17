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


'''
LIST TO DO:
* Make a service for getting lesson for a day.
* Get a class from a lesson. (list of lessons)
* Now with all the classes from that day, get info from classes i.e. Teacher Name, Level etc
* Display in reg_view

Funtions needed (for services):
* Get lesson from day (put in a day and get list of lessons)
* Get a class from a lesson.
* Get teacher name using teacher_id
___________________________________

LessonService, ClassService, TeacherService

Controllers needed: ***
These controller
'''