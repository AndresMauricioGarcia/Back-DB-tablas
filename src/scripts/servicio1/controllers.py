from flask import jsonify
from .queries import (
    fetch_pokemons, fetch_abilities, fetch_types, fetch_pokemon_abilities, fetch_pokemon_types
)

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
