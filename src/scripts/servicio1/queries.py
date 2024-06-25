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


# metodo PUT


def update_pokemon(pokemon_id, name, base_experience, height, weight):
    query = "UPDATE pokemon SET name=%s, base_experience=%s, height=%s, weight=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, base_experience, height, weight, pokemon_id))


def update_ability(ability_id, name, is_hidden, slot, effect):
    query = "UPDATE abilities SET name=%s, is_hidden=%s, slot=%s, effect=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, is_hidden, slot, effect, ability_id))


def update_type(type_id, name):
    query = "UPDATE types SET name=%s WHERE id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (name, type_id))


def update_pokemon_ability(pokemon_id, ability_id, new_ability_id):
    query = "UPDATE pokemon_abilities SET ability_id=%s WHERE pokemon_id=%s AND ability_id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (new_ability_id, pokemon_id, ability_id))


def update_pokemon_type(pokemon_id, type_id, new_type_id):
    query = "UPDATE pokemon_types SET type_id=%s WHERE pokemon_id=%s AND type_id=%s"
    with db._open_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (new_type_id, pokemon_id, type_id))
