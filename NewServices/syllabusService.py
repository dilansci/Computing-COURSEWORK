import SQL_controller

class SOWService():
# will contain  SQL queries for fetch SOW data from the db.
    def __init__(self, sqlcontroller: SQL_controller.SQLController):
        self.control = sqlcontroller