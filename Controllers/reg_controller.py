

class RegController():

    def __init__(self, service):
        super().__init__()
        self.reg_service = service # lessonService
        print("This is RegService!",self.reg_service)
    
    def reg_factory(self, day):
        return self.reg_service.get_lessons_day(day) # fix this. No link with service.
        