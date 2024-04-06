
class SOWController():
# this will contain links to 'syllabusService'
    def __init__(self, sow_service, day_service, class_service):
        super().__init__()
        self.sow_service = sow_service
        self.day_service = day_service
        self.class_service = class_service
    
    def get_sow(self, sow_id):
        return self.sow_service.get_sow(sow_id)
    
    def get_mark(self, swimmer_id):
        return self.day_service.get_mark(swimmer_id)
    
    def get_skills(self, level_num):
        return self.sow_service.get_skills(level_num)
    
    def get_swimmer(self, swimmer_id):
        return self.day_service.get_swimmer(swimmer_id)[0]
    
    def get_swimmer_level(self, class_id):
        return self.class_service.get_swimmer_level(class_id)
