import sqlite3
from urllib.request import pathname2url
import datetime


class Database:

    """
    check if the database exsits already
    """
    @staticmethod
    def checkdbConnection():
        try:
            con = sqlite3.connect('file:sensehat.db?mode=rw', uri=True)
            print('Establishing a connection...')
            return con
        except sqlite3.OperationalError:
            print('Creating tables...')
            Database.createTables()
            con = sqlite3.connect('sensehat.db')
            return con

    """
    creates tables if the database doesn't exist
    """
    @staticmethod
    def createTables():
        con = sqlite3.connect('sensehat.db')
        with con:
            cur = con.cursor()
            cur.execute("""CREATE TABLE SENSEHAT_data (
                timestamp DATETIME,
                temp NUMERIC,
                humidity NUMERIC
                )""")

            cur.execute("""CREATE TABLE NOTIFICATION_data(
                timestamp DATETIME
                )""")

    """
    logs temperature and humidity data
    """
    @staticmethod
    def logTempHumData(timestamp, temp, humidity):
        conn = Database.checkdbConnection()
        curs = conn.cursor()
        curs.execute("""INSERT INTO SENSEHAT_data
                        values((?), (?), (?))""", (timestamp, temp, humidity,))
        conn.commit()
        conn.close()

    """
    logs notification data
    """
    @staticmethod
    def logNotificationData(timestamp):
        conn = Database.checkdbConnection()
        curs = conn.cursor()
        curs.execute("""INSERT INTO NOTIFICATION_data
                        values((?))""", (timestamp,))
        conn.commit()
        conn.close()

    """
    Gets all the temperature and humidity data from database
    """
    @staticmethod
    def getAllSenseHatData():
        conn = Database.checkdbConnection()
        curs = conn.cursor()
        curs.execute("SELECT * FROM SENSEHAT_data")
        senseHatData = curs.fetchall()
        conn.close()
        return senseHatData

    """
    checks if the notification has been sent already for a given date
    (date format '2019-03-25')
    """
    @staticmethod
    def hasNotified(time):
        # gets the last notification sent from database
        lastNotify = Database.getLastNotification()
        if lastNotify is None:
            print('we haven\'t sent a notification today')
            return False
        else:
            # converts utc time to local time
            localtimestamp = Database.getLocalTime(lastNotify)
            # convert local timestamp to local date
            localDate = Database.getDateFromTimestamp(localtimestamp[0])
            currentDate = Database.getDateFromTimestamp(str(time))
            print(localDate)
            if localDate == currentDate:
                print('Last notification in database match today')
                return True
            else:
                print('we haven\'t sent a notification today')
                return False

    @staticmethod
    def getLastNotification():
        if not Database.isNotificationDBEmpty():
            conn = Database.checkdbConnection()
            curs = conn.cursor()
            curs.execute("""SELECT * FROM NOTIFICATION_data
                            ORDER BY timestamp DESC LIMIT 1
                        """)
            last = curs.fetchone()
            conn.close()
            return last
        else:
            return None

    @staticmethod
    def isNotificationDBEmpty():
        conn = Database.checkdbConnection()
        curs = conn.cursor()
        curs.execute("""SELECT * FROM NOTIFICATION_data""")
        data = curs.fetchone()
        conn.close()
        if data is None:
            return True
        else:
            return False

    @staticmethod
    def getDateFromTimestamp(timestamp):
        return timestamp.split(' ', 1)[0]

    @staticmethod
    def getLocalTime(timestamp):
        # create a conversion that converts utc to local time
        return timestamp
