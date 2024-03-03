import SQL_controller

class SOWService():
# will contain  SQL queries for fetch SOW data from the db.
    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
    
    def get_sow_level(self, sow_id):
        return self.control.run_execute("SELECT intro,main,contrast,pool_depth FROM SOW WHERE sow_ID=?",sow_id)[0]