
class DayController():
    
    def __init__(self, service):
        super().__init__()
        self.day_service = service
        print("This is DayService!",self.day_service)

