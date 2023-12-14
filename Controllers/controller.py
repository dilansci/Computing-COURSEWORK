import sqlite3

'''
The controller is where all the code is processed. It gains data from the 'model.py' file and uses that data to perform 
various acttions.
This controller also
'''

class SQLController():
    # establishing the viw for this controller !* might change as im not sure if this is reusable *!
    def __init__(self, view):
        super().__init__()
        self.view = view
        # this establishes a connection between the 'controller/view' files and the 'sqlite3 database'.
        self.conn = sqlite3.connect("swimmers.db")
        self.cursor = self.conn.cursor()
    
    # CLASS 'change_day_reg' doesn't work yet ***
    def change_day_reg(self, day):
        day = day.strip()
        print(f"Control \"{day}\"")
        self.cursor.execute(f'SELECT first_name,last_name FROM Swimmers WHERE day=?', [day]) # find a way to access 'Class' field from 'Swimmers' ¬¬¬ INNER JOIN Class ON Swimmers.day = Class.class_day
        current_reg = self.cursor.fetchall()
        return(current_reg) # return value to day_view to be put into the UI
    
    def reg_factory(self, day):

        pass
    '''
    find a way to either: 
    1. Get an interactive listbox, so that when you click on a name it comes up.
    2. Use Label Frames to store Buttons for Register and the list of swimmers.
    '''

        ## currently trying to connect to database to store values on swimmers, classes and levels etc.
if __name__ == "__main__":
    control = SQLController()
    control.mainloop()
        