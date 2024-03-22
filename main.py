import mysql.connector

class DatabaseConnection:
    def _init_(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            port=3306,
            database="advance_python"
        )
        self.cursor = self.connection.cursor()



