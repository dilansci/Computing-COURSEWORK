
class ClassController():

    def __init__(self, class_service, reg_service, day_service, sow_service):
        super().__init__()
        self.class_service = class_service
        self.reg_service = reg_service
        self.day_service = day_service
        self.sow_service = sow_service
    
    def get_swimmers_from_class(self, class_id):
        return self.class_service.get_swimmers_from_class(class_id)
    
    def get_teacher_name(self, teacher_id):
        return self.reg_service.get_teacher_name(teacher_id)

    def get_class_day(self, class_id):
        return self.class_service.get_class_day(class_id)

    def get_class(self):
        return self.reg_service.get_class()
    
    def get_all_classes_ids(self):
        return self.class_service.get_all_classes_ids()

    def get_all_swimmers(self):
        return self.class_service.get_all_swimmers()

    def get_teacher_name(self, teacher_id):
        return self.reg_service.get_teacher_name(teacher_id)[0]

    def get_all_teachers(self):
        return self.class_service.get_all_teachers()

    def get_all_teachers_id(self):
        return self.class_service.get_all_teachers_id()
    
    def get_all_classes(self):
        return self.class_service.get_all_classes()

    def get_sow(self, sow_id):
        return self.sow_service.get_sow(sow_id)
    
    def update_class_teacher(self, teacher_id, class_id):
        return self.class_service.update_class_teacher(teacher_id, class_id)
    
    def update_class_level(self, new_level, class_id):
        return self.class_service.update_class_level(new_level, class_id)
    
    def update_class_sow(self, sow_label, new_data, sow_id):
        return self.class_service.update_class_sow(sow_label, new_data, sow_id)
    
    def update_swimmer_info(self, swimmer_id, f_name, l_name, email, phone):
        return self.class_service.update_swimmer_info(swimmer_id, f_name, l_name, email, phone)
    
    def update_swimmer_class_id(self, class_id, swimmer_id):
        return self.class_service.update_swimmer_class_id(class_id, swimmer_id)
    
    def update_class_info(self, class_id, level, time, teacher_id, day):
        return self.class_service.update_class_info(class_id, level, time, teacher_id, day)
    
    def add_class(self, level, time, teacher_id, day):
        return self.class_service.add_class(level, time, teacher_id, day)
    
    def remove_class(self, class_id):
        return self.class_service.remove_class(class_id)