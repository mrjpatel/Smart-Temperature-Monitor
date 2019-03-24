import sqlite3
from urllib.request import pathname2url

class Database:

    dbname = 'sensehat.db'

    #check if the database exsits already
    def dbConnect(self):
        try:
            con = sqlite3.connect('file:sensehat.db?mode=rw', uri=True)
            print('Establishing a connection...')
            # return con
        except sqlite3.OperationalError:
            print('Creating tables...')
            self.createTables()
            
    # creates tables if the database doesn't exist
    def createTables(self):
        con = sqlite3.connect(Database.dbname)
        with con:
            cur = con.cursor() 
            cur.execute("""CREATE TABLE SENSEHAT_data (
                timestamp DATETIME,
                temp NUMERIC,
                humidity NUMERIC
                )""")

            cur.execute("""CREATE TABLE NOTIFICATION_data(
                timestamp DATETIME,
                notified NUMERIC
                )""")

database = Database()
database.dbConnect()
