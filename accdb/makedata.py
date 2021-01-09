
import pyodbc

conn = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:/Users/Gebruiker/Documents/Python/Erp4.accdb')
cursor = conn.cursor()

class makedata():

    def __init__(self):
        self.itemsforcode = []
        self.itemdict = dict()       
        self.length = 0

    def dbitems(self):
        #This function gets data from a table, and appends it to a list.       
        cursor.execute("select * from TijdVerantwoording")
        for row in cursor.fetchall():
            self.itemsforcode.append([row.Opmerking, row.Datum, row.Duur])
        self.length = len(self.itemsforcode)

    def dictitems(self):
        #Get DB Items
        self.dbitems()

        key = 'key'
        date = '01-01-2020'
        for i in range(self.length):
            date = str(self.itemsforcode[i][1])[:-9]
            self.itemdict[key+str(i)]={'opmerking': self.itemsforcode[i][0], 'datum': date, 'aantal uur': self.itemsforcode[i][2]}
        return self.itemdict
