from ..connection import DBConnection

db = DBConnection()

def fetch_locations():
    query = "SELECT * FROM locations"
    with db.open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def fetch_characters():
    query = "SELECT * FROM characters"
    with db.open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def fetch_episodes():
    query = "SELECT * FROM episodes"
    with db.open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def fetch_character_episodes():
    query = "SELECT * FROM character_episodes"
    with db.open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
