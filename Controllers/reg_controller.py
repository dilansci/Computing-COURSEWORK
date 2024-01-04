import SQL_controller
from NewServices.lessonService import LessonService

class RegController():
    # need to update RegController. Remove SQL connection.
    def __init__(self, view):
        ## prob dont need this SQL connection in constructor as we have SQLcontroller
        super().__init__()
        self.view = view
        self.service = LessonService(SQL_controller.SQLController) # i think this is the correct parameter?
    
    def reg_factory(self, day):
        self.service.get_lessons_day(day)
        