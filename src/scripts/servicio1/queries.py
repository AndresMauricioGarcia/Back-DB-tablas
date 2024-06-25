from ..connection import Connection
from psycopg2.extras import RealDictCursor

db = Connection()

# Metodo GET

def fetch_pokemons(page=1, limit=3):
    offset = (page - 1) * limit
    query = "SELECT * FROM pokemon LIMIT %s OFFSET %s"
    with db._open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (limit, offset))
            pokemons = cursor.fetchall()
    return {pokemon['id']: pokemon for pokemon in pokemons}


def fetch_abilities(page=1, limit=3):
    offset = (page - 1) * limit
    query = "SELECT * FROM abilities LIMIT %s OFFSET %s"
    with db._open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (limit, offset))
            abilities = cursor.fetchall()
    return {ability['id']: ability for ability in abilities}


def fetch_types(page=1, limit=3):
    offset = (page - 1) * limit
    query = "SELECT * FROM types LIMIT %s OFFSET %s"
    with db._open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (limit, offset))
            types = cursor.fetchall()
    return {type_['id']: type_ for type_ in types}


def fetch_pokemon_abilities(page=1, limit=3):
    offset = (page - 1) * limit
    query = "SELECT * FROM pokemon_abilities LIMIT %s OFFSET %s"
    with db._open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (limit, offset))
            pokemon_abilities = cursor.fetchall()
    return {pokemon_ability['pokemon_id']: pokemon_ability for pokemon_ability in pokemon_abilities}


def fetch_pokemon_types(page=1, limit=3):
    offset = (page - 1) * limit
    query = "SELECT * FROM pokemon_types LIMIT %s OFFSET %s"
    with db._open_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(query, (limit, offset))
            pokemon_types = cursor.fetchall()
    return {pokemon_type['pokemon_id']: pokemon_type for pokemon_type in pokemon_types}

# Metodo POST


def insert_pokemon(name, base_experience, height, weight):
    query = "INSERT INTO pokemon (name, base_experience, height, weight) VALUES (%s, %s, %s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, base_experience, height, weight))
            conn.commit()


def insert_ability(name, is_hidden, slot, effect):
    query = (
        "INSERT INTO abilities (name, is_hidden, slot, effect) VALUES (%s, %s, %s, %s)"
    )
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, is_hidden, slot, effect))
            conn.commit()


def insert_type(name):
    query = "INSERT INTO types (name) VALUES (%s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name,))
            conn.commit()


def insert_pokemon_ability(pokemon_id, ability_id):
    query = "INSERT INTO pokemon_abilities (pokemon_id, ability_id) VALUES (%s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (pokemon_id, ability_id))
            conn.commit()


def insert_pokemon_type(pokemon_id, type_id):
    query = "INSERT INTO pokemon_types (pokemon_id, type_id) VALUES (%s, %s)"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (pokemon_id, type_id))
            conn.commit()


# Metodo PUT


def update_pokemon(pokemon_id, name, base_experience, height, weight):
    query = "UPDATE pokemon SET name=%s, base_experience=%s, height=%s, weight=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, base_experience, height, weight, pokemon_id))
            conn.commit()


def update_ability(ability_id, name, is_hidden, slot, effect):
    query = "UPDATE abilities SET name=%s, is_hidden=%s, slot=%s, effect=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, is_hidden, slot, effect, ability_id))
            conn.commit()


def update_type(type_id, name):
    query = "UPDATE types SET name=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, type_id))
            conn.commit()


def update_pokemon_ability(pokemon_id, ability_id, new_ability_id):
    query = "UPDATE pokemon_abilities SET ability_id=%s WHERE pokemon_id=%s AND ability_id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (new_ability_id, pokemon_id, ability_id))
            conn.commit()


def update_pokemon_type(pokemon_id, type_id, new_type_id):
    query = "UPDATE pokemon_types SET type_id=%s WHERE pokemon_id=%s AND type_id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (new_type_id, pokemon_id, type_id))
            conn.commit()
