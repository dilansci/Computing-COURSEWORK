

class RegController():

    def __init__(self, service):
        super().__init__()
        self.reg_service = service
        print("This is RegService!",self.reg_service)
    
    def reg_factory(self, day):
        self.reg_service.get_lessons_day(day) # fix this. No link with service.
        