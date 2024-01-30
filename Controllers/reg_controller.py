
class RegController():

    def __init__(self, service, day_service):
        super().__init__()
        self.reg_service = service 
        self.swim_service = day_service

    def get_swimmer_name(self, class_id):
        return self.swim_service.get_swimmer_name(class_id)
        