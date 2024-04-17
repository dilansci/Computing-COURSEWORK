
class DayController():
    
    def __init__(self, day_service, reg_service):
        super().__init__()
        self.day_service = day_service
        self.reg_service = reg_service

    def get_swimmers(self):
        return self.day_service.get_swimmers()
    
    def get_class(self, teacher_id):
        return self.reg_service.get_class(teacher_id)
    
    def get_teacher_name(self, teacher_id):
        return self.reg_service.get_teacher_name(teacher_id)
    
    def get_lessons_day(self, day):
        return self.day_service.get_lessons_day(day)
    
    def get_sow(self, sow_id):
        return self.reg_service.get_sow(sow_id)
    
    def get_send(self, swimmer_id):
        return self.day_service.get_send(swimmer_id)
    
    def add_swimmer(self, f_name, l_name, email, phone):
        return self.day_service.add_swimmer(f_name, l_name, email, phone)
    
    def update_swimmer_info(self, swimmer_id, f_name, l_name, email, phone):
        return self.day_service.update_swimmer_info(swimmer_id, f_name, l_name, email, phone)
    
    def update_send(self, swimmer_id, send):
        return self.day_service.update_send(swimmer_id, send)