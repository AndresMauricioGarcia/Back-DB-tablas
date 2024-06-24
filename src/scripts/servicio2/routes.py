from flask import Blueprint
from .controllers import (
    get_locations, get_characters, get_episodes, get_character_episodes
)

rick_and_morty_blueprint = Blueprint(
    "rick_and_morty_blueprint",
    __name__,
    url_prefix='/rick_and_morty'
)

rick_and_morty_blueprint.add_url_rule(
    "/locations",
    view_func=get_locations,
    methods=["GET"]
)

rick_and_morty_blueprint.add_url_rule(
    "/characters",
    view_func=get_characters,
    methods=["GET"]
)

rick_and_morty_blueprint.add_url_rule(
    "/episodes",
    view_func=get_episodes,
    methods=["GET"]
)

rick_and_morty_blueprint.add_url_rule(
    "/character_episodes",
    view_func=get_character_episodes,
    methods=["GET"]
)
