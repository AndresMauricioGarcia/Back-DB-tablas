from ..connection import Connection
from psycopg2.extras import RealDictCursor

db = Connection()

# Metodo GET

def fetch_locations(page=1, limit=3):
    offset = (page - 1) * limit
    query = "SELECT * FROM locations LIMIT %s OFFSET %s"
    with db._open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (limit, offset))
            locations = cursor.fetchall()
    return {location['id']: location for location in locations}


def fetch_characters(page=1, limit=3):
    offset = (page - 1) * limit
    query = "SELECT * FROM characters LIMIT %s OFFSET %s"
    with db._open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (limit, offset))
            characters = cursor.fetchall()
    return {character['id']: character for character in characters}


def fetch_episodes(page=1, limit=3):
    offset = (page - 1) * limit
    query = "SELECT * FROM episodes LIMIT %s OFFSET %s"
    with db._open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (limit, offset))
            episodes = cursor.fetchall()
    return {episode['id']: episode for episode in episodes}


def fetch_character_episodes(page=1, limit=3):
    offset = (page - 1) * limit
    query = "SELECT * FROM character_episodes LIMIT %s OFFSET %s"
    with db._open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (limit, offset))
            character_episodes = cursor.fetchall()
    return {character_episode['character_id']: character_episode for character_episode in character_episodes}


# Metodo POST


def insert_location(name, type, dimension):
    query = "INSERT INTO locations (name, type, dimension) VALUES (%s, %s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, type, dimension))
            conn.commit()


def insert_character(name, status, species, gender, location_id):
    query = "INSERT INTO characters (name, status, species, gender, location_id) VALUES (%s, %s, %s, %s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, status, species, gender, location_id))
            conn.commit()


def insert_episode(name, air_date, episode_code):
    query = "INSERT INTO episodes (name, air_date, episode_code) VALUES (%s, %s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, air_date, episode_code))
            conn.commit()


def insert_character_episode(character_id, episode_id):
    query = "INSERT INTO character_episodes (character_id, episode_id) VALUES (%s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (character_id, episode_id))
            conn.commit()


# Metodo PUT


def update_location(location_id, name, type, dimension):
    query = "UPDATE locations SET name=%s, type=%s, dimension=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, type, dimension, location_id))
            conn.commit()


def update_character(character_id, name, status, species, gender, location_id):
    query = "UPDATE characters SET name=%s, status=%s, species=%s, gender=%s, location_id=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                query, (name, status, species, gender, location_id, character_id)
            )
            conn.commit()


def update_episode(episode_id, name, air_date, episode_code):
    query = "UPDATE episodes SET name=%s, air_date=%s, episode_code=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, air_date, episode_code, episode_id))
            conn.commit()


def update_character_episode(character_id, episode_id, new_episode_id):
    query = "UPDATE character_episodes SET episode_id=%s WHERE character_id=%s AND episode_id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (new_episode_id, character_id, episode_id))
            conn.commit()
