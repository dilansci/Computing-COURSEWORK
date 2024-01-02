import sqlite3

class RegController():

    def __init__(self, view):
        super().__init__()
        self.view = view
        # establish connection with SQL database
        self.conn = sqlite3.connect("swimmers.db")
        self.cursor = self.conn.cursor()
    
    def change_day_reg(self, day):
        self.cursor.execute('''SELECT COUNT(class_ID) as classCount FROM Class''')
        classCount = self.cursor.fetchall()
        for count in classCount:
            r, c = 1, 0
            self.reg_button = tk.Button(self, text=f"Register(classCount)").grid(row=r, column=c)