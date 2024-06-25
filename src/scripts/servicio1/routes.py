# src/scripts/servicio1/routes.py
from flask import Blueprint
from .controllers import (
    get_pokemons,
    get_abilities,
    get_types,
    get_pokemon_abilities,
    get_pokemon_types,
    add_pokemon,
    add_ability,
    add_type,
    add_pokemon_ability,
    add_pokemon_type,
)

# metodo GET

servicio1_blueprint = Blueprint(
    "servicio1_blueprint", __name__, url_prefix="/servicio1"
)

servicio1_blueprint.add_url_rule("/pokemons", view_func=get_pokemons, methods=["GET"])

servicio1_blueprint.add_url_rule("/abilities", view_func=get_abilities, methods=["GET"])

servicio1_blueprint.add_url_rule("/types", view_func=get_types, methods=["GET"])

servicio1_blueprint.add_url_rule(
    "/pokemon_abilities", view_func=get_pokemon_abilities, methods=["GET"]
)

servicio1_blueprint.add_url_rule(
    "/pokemon_types", view_func=get_pokemon_types, methods=["GET"]
)

servicio1_blueprint.add_url_rule("/pokemons", view_func=add_pokemon, methods=["POST"])

# metodo POST

servicio1_blueprint.add_url_rule("/abilities", view_func=add_ability, methods=["POST"])

servicio1_blueprint.add_url_rule("/types", view_func=add_type, methods=["POST"])

servicio1_blueprint.add_url_rule(
    "/pokemon_abilities", view_func=add_pokemon_ability, methods=["POST"]
)

servicio1_blueprint.add_url_rule(
    "/pokemon_types", view_func=add_pokemon_type, methods=["POST"]
)
