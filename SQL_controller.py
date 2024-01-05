import sqlite3


class SQLController():
    # establishing the view for this controller !* might change as im not sure if this is reusable *!
    def __init__(self):
        super().__init__()
        # this establishes a connection between the 'controller/view' files and the 'sqlite3 database'.
        self.conn = sqlite3.connect("swimmers.db")
        self.cursor = self.conn.cursor()

    def run_execute(self, statement, *args):
        # 'statement' is the actual SQL command
        self.cursor.execute(statement, args)
        self.data = self.cursor.fetchall()
        return self.data
        # this returns the output for the SQL statements used in the services.

    '''
    find a way to either: 
    1. Get an interactive listbox, so that when you click on a name it comes up.
    2. Use Label Frames to store Buttons for Register and the list of swimmers.
    ''' 