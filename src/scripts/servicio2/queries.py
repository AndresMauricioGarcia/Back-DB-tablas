from ..connection import Connection

db = Connection()

def fetch_locations():
    query = "SELECT * FROM locations"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def fetch_characters():
    query = "SELECT * FROM characters"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def fetch_episodes():
    query = "SELECT * FROM episodes"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def fetch_character_episodes():
    query = "SELECT * FROM character_episodes"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
