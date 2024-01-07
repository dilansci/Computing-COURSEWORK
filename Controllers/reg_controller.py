

class RegController():

    def __init__(self, service):
        super().__init__()
        self.reg_service = service # lessonService
        print("This is RegService!",self.reg_service)
    
    # def reg_factory(self, day):
    #     return self.reg_service.get_lessons_day(day) # fix this. No link with service.
        ''' 
        Don't think ill need this 'reg_factory'??
        Not sure what to do with this controller yet.
        Currently keeping it as a link for 'lessonService' so that
        '''
        