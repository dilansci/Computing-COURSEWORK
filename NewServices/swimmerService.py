import SQL_controller

class SwimmerService():
    
    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller

    def get_swimmers(self):
        return self.control.execute("SELECT * FROM Swimmers")
    
    def get_lessons_day(self, day):
        print("This is the SQL output!",self.control.execute("SELECT * FROM Lessons WHERE day=?",day))
        return self.control.execute("SELECT * FROM Lessons WHERE day=?",day)

    def get_swimmer(self, id):
        return self.control.execute("SELECT * FROM Swimmers WHERE swimmer_ID =?",id)

    
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
