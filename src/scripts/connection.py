import os
from contextlib import contextmanager
from typing import Generator
from psycopg2 import connect, OperationalError, extensions
from psycopg2.extras import RealDictCursor
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class DBConnection:
    def __init__(self):
        self.db_info = {
            'dbname': os.getenv('DB_DBNAME'),
            'user': os.getenv('DB_USER'),
            'password': os.getenv('DB_PASSWORD'),
            'host': os.getenv('DB_HOST'),
            'port': os.getenv('DB_PORT')
        }

    @contextmanager
    def open_connection(self) -> Generator[extensions.connection, None, None]:
        conn = None
        try:
            conn = connect(**self.db_info)
            yield conn
        except OperationalError as e:
            print(f"Error connecting to the database: {e}")
        finally:
            if conn:
                conn.close()
