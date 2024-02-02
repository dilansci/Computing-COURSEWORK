import SQL_controller

class SOWService():
# will contain  SQL queries for fetch SOW data from the db.
    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller
    
    def get_sow_level(self, level_num):
        return self.control.run_execute("SELECT intro,main,contrast,pool_depth FROM SOW WHERE level_num=? AND week_num=1",level_num)