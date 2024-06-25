from ..connection import Connection

db = Connection()

# metodo GET


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


# metodo POST


def insert_pokemon(name, base_experience, height, weight):
    query = "INSERT INTO pokemon (name, base_experience, height, weight) VALUES (%s, %s, %s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, base_experience, height, weight))


def insert_ability(name, is_hidden, slot, effect):
    query = (
        "INSERT INTO abilities (name, is_hidden, slot, effect) VALUES (%s, %s, %s, %s)"
    )
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, is_hidden, slot, effect))


def insert_type(name):
    query = "INSERT INTO types (name) VALUES (%s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name,))


def insert_pokemon_ability(pokemon_id, ability_id):
    query = "INSERT INTO pokemon_abilities (pokemon_id, ability_id) VALUES (%s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (pokemon_id, ability_id))


def insert_pokemon_type(pokemon_id, type_id):
    query = "INSERT INTO pokemon_types (pokemon_id, type_id) VALUES (%s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (pokemon_id, type_id))
