from flask import jsonify
from .queries import (
    fetch_locations, fetch_characters, fetch_episodes, fetch_character_episodes
)

def get_locations():
    return jsonify(fetch_locations())

def get_characters():
    return jsonify(fetch_characters())

def get_episodes():
    return jsonify(fetch_episodes())

def get_character_episodes():
    return jsonify(fetch_character_episodes())
