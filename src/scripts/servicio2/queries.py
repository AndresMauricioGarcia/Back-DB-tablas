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


# metodo PUT


def update_location(location_id, name, type, dimension):
    query = "UPDATE locations SET name=%s, type=%s, dimension=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, type, dimension, location_id))


def update_character(character_id, name, status, species, gender, location_id):
    query = "UPDATE characters SET name=%s, status=%s, species=%s, gender=%s, location_id=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                query, (name, status, species, gender, location_id, character_id)
            )


def update_episode(episode_id, name, air_date, episode_code):
    query = "UPDATE episodes SET name=%s, air_date=%s, episode_code=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, air_date, episode_code, episode_id))


def update_character_episode(character_id, episode_id, new_episode_id):
    query = "UPDATE character_episodes SET episode_id=%s WHERE character_id=%s AND episode_id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (new_episode_id, character_id, episode_id))
