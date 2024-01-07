import SQL_controller

class LessonService():
    ## The 'sqlcontroller' will be a link to the database in SQL 
    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
    
    def get_lessons_day(self, day):
        return self.control.run_execute("SELECT * FROM Lessons WHERE day=?", day)