from mysql.connector import Error, connect
from contextlib import contextmanager

class Database:
    def __init__(self):
        self._config = {
            "host": "localhost",
            "user": "root",  # Thay bằng username MySQL
            "password": "",  # Thay bằng password MySQL
            "database": "students_db"
        }
    
    @contextmanager
    def get_connection(self):
        connection = None
        try:
            connection = connect(**self._config)
            yield connection
        except Error as e:
            raise Exception(f"Database error: {e}")
        finally:
            if connection and connection.is_connected():
                connection.close()