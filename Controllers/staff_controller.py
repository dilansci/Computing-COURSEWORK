
class StaffController():

    def __init__(self, staff_service):
        super().__init__()
        self.staff_service = staff_service
    
    def get_teachers(self):
        return self.staff_service.get_teachers()

    def get_assistants(self):
        return self.staff_service.get_assistants()
    
    def get_teacher_info(self, fname, lname):
        return self.staff_service.get_teacher_info(fname, lname)
    
    def get_access_level(self, fname, lname):
        return self.staff_service.get_access_level(fname, lname)
    
    def update_staff_info(self, staff_id, fname, lname, pin, email, phone, access_level):
        return self.staff_service.update_teacher_info(staff_id, fname, lname, pin, email, phone, access_level)
