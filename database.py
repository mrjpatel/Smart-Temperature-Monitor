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
        conn.close()

    # Gets all the temperature and humidity data from database
    def getAllSenseHatData (self):	
        conn = self.checkdbConnection()
        curs = conn.cursor()
        curs.execute("SELECT * FROM SENSEHAT_data")
        senseHatData = curs.fetchall()
        conn.close()
        return senseHatData

    # checks if the notification has been sent already for a given date ( date format '2019-03-25')
    def hasNotified (self, timestamp):	
        conn = self.checkdbConnection()
        curs = conn.cursor()
        curs.execute("SELECT * FROM NOTIFICATION_data WHERE timestamp=:timestamp", {"timestamp": timestamp})
        notificationValue = curs.fetchone()
        if notificationValue is not None:
            print("The notification has already been sent")
            print(notificationValue)
            return True
        else:
            print("Notification has not been sent")
            return False
        conn.commit()
        conn.close()

