
class DayController():
    
    def __init__(self, service, reg_service):
        super().__init__()
        self.day_service = service
        self.reg_service = reg_service
        print("This is DayService!",self.day_service)

