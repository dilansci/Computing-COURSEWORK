
class RegController():

    def __init__(self, reg_service, day_service):
        super().__init__()
        self.reg_service = reg_service 
        self.day_service = day_service

    def get_swimmer_name(self, class_id):
        return self.day_service.get_swimmer_name(class_id)   
    
    def get_attendance(self, class_id):
        return self.reg_service.get_attendance(class_id)
    
    def set_attendance(self, swimmer_id, attendance_data):
        return self.reg_service.set_attendance(swimmer_id, attendance_data)

    def get_swimmers_in_class(self, class_id):
        return self.day_service.get_swimmers_in_class(class_id)
    
    def get_swimmer(self, swimmer_id):
        return self.day_service.get_swimmer(swimmer_id)