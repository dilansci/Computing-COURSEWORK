

class RegController():

    def __init__(self, service):
        super().__init__()
        self.reg_service = service # lessonService
        print("This is RegService!",self.reg_service)

        ''' 
        Don't think ill need this 'reg_factory'??
        Not sure what to do with this controller yet.
        Currently keeping it as a link for 'lessonService' so that
        '''
        