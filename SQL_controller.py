import sqlite3

class SQLController():

    def __init__(self):
        super().__init__()
        # this establishes a connection between the 'controller/view' files and the 'sqlite3 database'.
        self.conn = sqlite3.connect("swimmers.db")
        self.cursor = self.conn.cursor()

    def run_execute(self, statement, *args):
        # 'statement' is the actual SQL command
        self.cursor.execute(statement, args)
        self.data = self.cursor.fetchall()
        self.conn.commit()
        return self.data # this returns the output for the SQL statements used in the services.
    