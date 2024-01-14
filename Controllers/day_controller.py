
class DayController():
    
    def __init__(self, service, reg_service):
        super().__init__()
        self.day_service = service
        self.reg_service = reg_service
        print("This is DayService!",self.day_service)

    def get_class(self, teacher_id):
        return self.reg_service.get_class(teacher_id)
    
    def get_teacher_name(self, teacher_id):
        return self.reg_service.get_teacher_name(teacher_id)
    
    def get_lessons_day(self, day):
        return self.day_service.get_lessons_day(day)
    
    def get_sow(self, sow_id):
        return self.reg_service.get_sow(sow_id)

