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
