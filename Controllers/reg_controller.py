
class RegController():

    def __init__(self, reg_service, day_service):
        super().__init__()
        self.reg_service = reg_service 
        self.swim_service = day_service

    def get_swimmer_name(self, class_id):
        return self.swim_service.get_swimmer_name(class_id)   
    
    def get_attendance(self, swimmer_names):
        return self.reg_service.get_attendance(swimmer_names)
    
    def set_attendance(self, swimmer_names, attendance_data):
        return self.reg_service.set_attendance(swimmer_names, attendance_data)