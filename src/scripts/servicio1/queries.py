from ..connection import Connection

db = Connection()

def fetch_pokemons():
    query = "SELECT * FROM pokemon"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def fetch_abilities():
    query = "SELECT * FROM abilities"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def fetch_types():
    query = "SELECT * FROM types"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def fetch_pokemon_abilities():
    query = "SELECT * FROM pokemon_abilities"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

def fetch_pokemon_types():
    query = "SELECT * FROM pokemon_types"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
