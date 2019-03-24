import sqlite3
from urllib.request import pathname2url
import datetime

class Database:

    dbname = 'sensehat.db'

    #check if the database exsits already
    def checkdbConnection(self):
        try:
            con = sqlite3.connect('file:sensehat.db?mode=rw', uri=True)
            print('Establishing a connection...')
            return con
        except sqlite3.OperationalError:
            print('Creating tables...')
            self.createTables()
            con = sqlite3.connect(Database.dbname)
            return con
            
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

    # logs temperature and humidity data
    def logTempHumData (self, timestamp, temp, humidity):	
        conn = self.checkdbConnection()
        curs = conn.cursor()
        curs.execute("INSERT INTO SENSEHAT_data values((?), (?), (?))", (timestamp, temp, humidity,))
        conn.commit()
        conn.close()

    # logs notification data
    def logNotificationData (self, timestamp, notified):	
        conn = self.checkdbConnection()
        curs = conn.cursor()
        curs.execute("INSERT INTO NOTIFICATION_data values((?), (?))", (timestamp, notified,))
        conn.commit()
        conn.close()

    

# database = Database()
# database.logNotifiedData(datetime.datetime.now(), 1)
