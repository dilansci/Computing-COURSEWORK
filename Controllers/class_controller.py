
class ClassController():

    def __init__(self, class_service, reg_service, day_service):
        super().__init__()
        self.class_service = class_service
        self.reg_service = reg_service
        self.day_service = day_service
    
    def get_class(self): # will get all info of a class to edit :)) (!!!NEED TO DO ASAP!!!)
        return self.reg_service.get_class()

    def get_teacher_name(self, teacher_id):
        return self.reg_service.get_teacher_name(teacher_id)[0]

    def get_all_teachers(self):
        return self.class_service.get_all_teachers()

    def get_all_teachers_id(self):
        return self.class_service.get_all_teachers_id()

    '''
    Going to rework the "View Class" function.
    Thinking of just adding a "Edit Class" button beside each class within "day_view".
    '''