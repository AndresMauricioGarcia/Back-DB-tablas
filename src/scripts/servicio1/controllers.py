from flask import request, jsonify
from .queries import (
    fetch_pokemons,
    fetch_abilities,
    fetch_types,
    fetch_pokemon_abilities,
    fetch_pokemon_types,
    insert_pokemon,
    insert_ability,
    insert_type,
    insert_pokemon_ability,
    insert_pokemon_type,
    update_pokemon,
    update_ability,
    update_type,
    update_pokemon_ability,
    update_pokemon_type,
)


# metodo GET
def get_pokemons():
    return jsonify(fetch_pokemons())


def get_abilities():
    return jsonify(fetch_abilities())


def get_types():
    return jsonify(fetch_types())


def get_pokemon_abilities():
    return jsonify(fetch_pokemon_abilities())


def get_pokemon_types():
    return jsonify(fetch_pokemon_types())


# metodo POST


def add_pokemon():
    data = request.json
    insert_pokemon(
        data["name"], data["base_experience"], data["height"], data["weight"]
    )
    return jsonify({"status": "success"}), 201


def add_ability():
    data = request.json
    insert_ability(data["name"], data["is_hidden"], data["slot"], data["effect"])
    return jsonify({"status": "success"}), 201


def add_type():
    data = request.json
    insert_type(data["name"])
    return jsonify({"status": "success"}), 201


def add_pokemon_ability():
    data = request.json
    insert_pokemon_ability(data["pokemon_id"], data["ability_id"])
    return jsonify({"status": "success"}), 201


def add_pokemon_type():
    data = request.json
    insert_pokemon_type(data["pokemon_id"], data["type_id"])
    return jsonify({"status": "success"}), 201


# metodo PUT


def edit_pokemon(pokemon_id):
    data = request.json
    update_pokemon(
        pokemon_id,
        data["name"],
        data["base_experience"],
        data["height"],
        data["weight"],
    )
    return jsonify({"status": "success"}), 200


def edit_ability(ability_id):
    data = request.json
    update_ability(
        ability_id, data["name"], data["is_hidden"], data["slot"], data["effect"]
    )
    return jsonify({"status": "success"}), 200


def edit_type(type_id):
    data = request.json
    update_type(type_id, data["name"])
    return jsonify({"status": "success"}), 200


def edit_pokemon_ability(pokemon_id, ability_id):
    data = request.json
    update_pokemon_ability(pokemon_id, ability_id, data["new_ability_id"])
    return jsonify({"status": "success"}), 200


def edit_pokemon_type(pokemon_id, type_id):
    data = request.json
    update_pokemon_type(pokemon_id, type_id, data["new_type_id"])
    return jsonify({"status": "success"}), 200
