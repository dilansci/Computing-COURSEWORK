
class ClassController():

    def __init__(self, class_service, reg_service, day_service, sow_service):
        super().__init__()
        self.class_service = class_service
        self.reg_service = reg_service
        self.day_service = day_service
        self.sow_service = sow_service
    
    def get_swimmers_from_class(self, class_id):
        return self.class_service.get_swimmers_from_class(class_id)

    def get_class(self): # will get all info of a class to edit :)) (!!!NEED TO DO ASAP!!!)
        return self.reg_service.get_class()

    def get_all_swimmers(self):
        return self.class_service.get_all_swimmers()

    def get_teacher_name(self, teacher_id):
        return self.reg_service.get_teacher_name(teacher_id)[0]

    def get_all_teachers(self):
        return self.class_service.get_all_teachers()

    def get_all_teachers_id(self):
        return self.class_service.get_all_teachers_id()

    def get_sow(self, sow_id):
        return self.sow_service.get_sow(sow_id)
    
    def update_class_teacher(self, teacher_id, class_id):
        return self.class_service.update_class_teacher(teacher_id, class_id)
    
    def update_class_level(self, new_level, class_id):
        return self.class_service.update_class_level(new_level, class_id)
    
    def update_class_sow(self, sow_label, new_data, sow_id):
        return self.class_service.update_class_sow(sow_label, new_data, sow_id)
    