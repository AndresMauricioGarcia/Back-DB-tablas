# src/scripts/pokemon/routes.py
from flask import Blueprint
from .controllers import (
    get_pokemons, get_abilities, get_types, get_pokemon_abilities, get_pokemon_types
)

pokemon_blueprint = Blueprint(
    "pokemon_blueprint",
    __name__,
    url_prefix='/pokemon'
)

pokemon_blueprint.add_url_rule(
    "/pokemons",
    view_func=get_pokemons,
    methods=["GET"]
)

pokemon_blueprint.add_url_rule(
    "/abilities",
    view_func=get_abilities,
    methods=["GET"]
)

pokemon_blueprint.add_url_rule(
    "/types",
    view_func=get_types,
    methods=["GET"]
)

pokemon_blueprint.add_url_rule(
    "/pokemon_abilities",
    view_func=get_pokemon_abilities,
    methods=["GET"]
)

pokemon_blueprint.add_url_rule(
    "/pokemon_types",
    view_func=get_pokemon_types,
    methods=["GET"]
)
