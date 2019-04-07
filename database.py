import sqlite3
from urllib.request import pathname2url
import datetime


class Database:

    """
    check if the database exsits already
    """
    @staticmethod
    def check_db_connection():
        try:
            con = sqlite3.connect('file:sensehat.db?mode=rw', uri=True)
            return con
        except sqlite3.OperationalError:
            Database.create_tables()
            con = sqlite3.connect('sensehat.db')
            return con

    """
    creates tables if the database doesn't exist
    """
    @staticmethod
    def create_tables():
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
        print('Missing Tables, tables created!')

    """
    logs temperature and humidity data
    """
    @staticmethod
    def log_temp_hum_data(timestamp, temp, humidity):
        conn = Database.check_db_connection()
        curs = conn.cursor()
        curs.execute("""INSERT INTO SENSEHAT_data
                        values((?), (?), (?))""", (timestamp, temp, humidity,))
        conn.commit()
        conn.close()
        print('Logged data in DB')

    """
    logs notification data
    """
    @staticmethod
    def log_notification_data(timestamp):
        conn = Database.check_db_connection()
        curs = conn.cursor()
        curs.execute("""INSERT INTO NOTIFICATION_data
                        values((?))""", (timestamp,))
        conn.commit()
        conn.close()
        print('Logged notification in DB')

    """
    Gets all the temperature and humidity data from database
    """
    @staticmethod
    def get_all_sensehat_data():
        conn = Database.check_db_connection()
        curs = conn.cursor()
        curs.execute("""SELECT * FROM SENSEHAT_data
                        ORDER BY timestamp ASC""")
        sensehat_data = curs.fetchall()
        conn.close()
        print('Retrieved all Data')
        return sensehat_data

    """
    Gets all the temperature data from database
    """
    @staticmethod
    def get_all_temperature_data():
        conn = Database.check_db_connection()
        curs = conn.cursor()
        curs.execute("""SELECT temp FROM SENSEHAT_data
                        ORDER BY timestamp ASC""")
        data = curs.fetchall()
        conn.close()
        print('Retrieved all Temperature Data')
        return data

    """
    Gets all the humidity data from database
    """
    @staticmethod
    def get_all_humidity_data():
        conn = Database.check_db_connection()
        curs = conn.cursor()
        curs.execute("""SELECT humidity FROM SENSEHAT_data
                        ORDER BY timestamp ASC""")
        data = curs.fetchall()
        conn.close()
        print('Retrieved all Humidity Data')
        return data

    """
    checks if the notification has been sent already for a given date
    (date format '2019-03-25')
    """
    @staticmethod
    def has_notified(time):
        # gets the last notification sent from database
        last_notify = Database.get_last_notification()
        if last_notify is None:
            return False
        else:
            # converts utc time to local time
            local_timestamp = Database.get_local_time(last_notify)
            # convert local timestamp to local date
            local_date = Database.get_date_from_timestamp(local_timestamp[0])
            current_date = Database.get_date_from_timestamp(str(time))
            print(local_date)
            if local_date == current_date:
                return True
            else:
                return False

    @staticmethod
    def get_last_notification():
        if not Database.is_notification_db_empty():
            conn = Database.check_db_connection()
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
    def is_notification_db_empty():
        conn = Database.check_db_connection()
        curs = conn.cursor()
        curs.execute("""SELECT * FROM NOTIFICATION_data""")
        data = curs.fetchone()
        conn.close()
        if data is None:
            return True
        else:
            return False

    @staticmethod
    def get_date_from_timestamp(timestamp):
        return timestamp.split(' ', 1)[0]

    @staticmethod
    def get_local_time(timestamp):
        # create a conversion that converts utc to local time
        return timestamp
