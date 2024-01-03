import sqlite3


class SQLController():
    # establishing the viw for this controller !* might change as im not sure if this is reusable *!
    def __init__(self, view):
        super().__init__()
        self.view = view
        # this establishes a connection between the 'controller/view' files and the 'sqlite3 database'.
        self.conn = sqlite3.connect("swimmers.db")
        self.cursor = self.conn.cursor()

    def execute(self, statement, *args):
        # 'statement' is the actual SQL command
        return self.cursor.execute(statement, args)
        
    
    
    '''
    find a way to either: 
    1. Get an interactive listbox, so that when you click on a name it comes up.
    2. Use Label Frames to store Buttons for Register and the list of swimmers.
    ''' 