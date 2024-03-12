import SQL_controller

class SOWService():

    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
    
    def get_sow(self, sow_id):
        return self.control.run_execute("SELECT intro,main,contrast,depth FROM SOW WHERE sow_ID=?",sow_id)[0]