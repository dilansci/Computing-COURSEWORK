
class SOWController():
# this will contain links to 'syllabusService'
    def __init__(self, sow_service):
        super().__init__()
        self.sow_service = sow_service
    
    def get_sow_level(self, level_num):
        return self.sow_service.get_sow_level(level_num)