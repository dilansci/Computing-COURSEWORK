
class ClassController():

    def __init__(self, class_service):
        super().__init__()
        self.class_service = class_service

    
    # use regService for this as they have the same method :))
    def get_classes(self):# will get all info of a class to edit :)) (!!!NEED TO DO ASAP!!!)
        return self.class_service.get_classes()