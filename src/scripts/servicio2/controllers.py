from flask import request, jsonify
from .queries import (
    fetch_locations,
    fetch_characters,
    fetch_episodes,
    fetch_character_episodes,
    insert_location,
    insert_character,
    insert_episode,
    insert_character_episode,
)


# metodo GET
def get_locations():
    return jsonify(fetch_locations())


def get_characters():
    return jsonify(fetch_characters())


def get_episodes():
    return jsonify(fetch_episodes())


def get_character_episodes():
    return jsonify(fetch_character_episodes())


# metodo POST


def add_location():
    data = request.json
    insert_location(data["name"], data["type"], data["dimension"])
    return jsonify({"status": "success"}), 201


def add_character():
    data = request.json
    insert_character(
        data["name"],
        data["status"],
        data["species"],
        data["gender"],
        data["location_id"],
    )
    return jsonify({"status": "success"}), 201


def add_episode():
    data = request.json
    insert_episode(data["name"], data["air_date"], data["episode_code"])
    return jsonify({"status": "success"}), 201


def add_character_episode():
    data = request.json
    insert_character_episode(data["character_id"], data["episode_id"])
    return jsonify({"status": "success"}), 201
