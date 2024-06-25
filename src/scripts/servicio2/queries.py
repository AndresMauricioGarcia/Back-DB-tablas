from ..connection import Connection

db = Connection()

# metodo GET


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


# metodo POST


def insert_location(name, type, dimension):
    query = "INSERT INTO locations (name, type, dimension) VALUES (%s, %s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, type, dimension))


def insert_character(name, status, species, gender, location_id):
    query = "INSERT INTO characters (name, status, species, gender, location_id) VALUES (%s, %s, %s, %s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, status, species, gender, location_id))


def insert_episode(name, air_date, episode_code):
    query = "INSERT INTO episodes (name, air_date, episode_code) VALUES (%s, %s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, air_date, episode_code))


def insert_character_episode(character_id, episode_id):
    query = "INSERT INTO character_episodes (character_id, episode_id) VALUES (%s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (character_id, episode_id))
