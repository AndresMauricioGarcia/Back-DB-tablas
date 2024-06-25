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
    edit_pokemon,
    edit_ability,
    edit_type,
    edit_pokemon_ability,
    edit_pokemon_type,
)



servicio1_blueprint = Blueprint(
    "servicio1_blueprint", __name__, url_prefix="/servicio1"
)

# metodo GET

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

# metodo PUT

servicio1_blueprint.add_url_rule(
    "/pokemons/<int:pokemon_id>", view_func=edit_pokemon, methods=["PUT"]
)

servicio1_blueprint.add_url_rule(
    "/abilities/<int:ability_id>", view_func=edit_ability, methods=["PUT"]
)

servicio1_blueprint.add_url_rule(
    "/types/<int:type_id>", view_func=edit_type, methods=["PUT"]
)

servicio1_blueprint.add_url_rule(
    "/pokemon_abilities/<int:pokemon_id>/<int:ability_id>",
    view_func=edit_pokemon_ability,
    methods=["PUT"],
)

servicio1_blueprint.add_url_rule(
    "/pokemon_types/<int:pokemon_id>/<int:type_id>",
    view_func=edit_pokemon_type,
    methods=["PUT"],
)
