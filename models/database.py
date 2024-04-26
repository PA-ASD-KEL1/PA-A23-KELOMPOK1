import mysql.connector
from mysql.connector import Error

class MySQLDatabase:
    def __init__(self, host="127.0.0.1", user="root", password="", database="ecofusion"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

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
                print("Connected to MySQL Server version", self.connection.get_server_info())
        except Error as e:
            print("Error while connecting to MySQL:", e)
            raise e  # Raise the exception for handling at higher levels

    def disconnect(self):
        if self.connection is not None and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")

class MySQLConnectionManager:
    _instance = None

    def __new__(cls, host="127.0.0.1", user="root", password="", database="ecofusion"):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.database = MySQLDatabase(host, user, password, database)
        return cls._instance

    def __init__(self, host="127.0.0.1", user="root", password="", database="ecofusion"):
        if self.database.connection is None:
            self.connect()

    def connect(self):
        self.database.connect()

    def get_connection(self):
        if self.database.connection is None:
            self.connect()
        return self.database.connection
