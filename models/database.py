import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                charset="utf8mb4"
            )
            if self.connection.is_connected():
                print("Connected to MariaDB Server version ", self.connection.get_server_info())
        except Error as e:
            print("Error while connecting to MariaDB", e)

    def disconnect(self):
        if self.connection.is_connected():
            self.connection.close()
            print("MariaDB connection is closed")
