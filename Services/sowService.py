import SQL_controller

class SOWService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
    
    def get_sow(self, sow_id):
        return self.control.run_execute("SELECT intro,main,contrast,depth FROM SOW WHERE sow_ID=?",sow_id)[0]
    
    def get_skills(self, level_num):
        return self.control.run_execute("SELECT skill_1, skill_2, skill_3, skill_4, skill_5 FROM Syllabus WHERE level_num=?", level_num)[0]