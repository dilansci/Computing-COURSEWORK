import sqlite3

class RegController():

    def __init__(self, view):
        ## prob dont need this SQL connection in constructor as we have SQLcontroller
        super().__init__()
        self.view = view
        ## needs 'controller' as parameter
        # establish connection with SQL database
        self.conn = sqlite3.connect("swimmers.db")
        self.cursor = self.conn.cursor()
    
    def reg_factory(self, day):
        self.cursor.execute('''SELECT * FROM Swimmers WHERE day=? ''', [day])
        classCount = self.cursor.fetchall()
        return(classCount)