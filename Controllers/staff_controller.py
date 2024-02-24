
class StaffController():

    def __init__(self, staff_service):
        super().__init__()
        self.staff_service = staff_service
    
    def get_teachers(self):
        return self.staff_service.get_teachers()

    def get_assistants(self):
        return self.staff_service.get_assistants()