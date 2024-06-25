from flask import Blueprint
from .controllers import (
    get_locations,
    get_characters,
    get_episodes,
    get_character_episodes,
    add_location,
    add_character,
    add_episode,
    add_character_episode,
    edit_location,
    edit_character,
    edit_episode,
    edit_character_episode,
)

servicio2_blueprint = Blueprint(
    "servicio2_blueprint", __name__, url_prefix="/servicio2"
)

# metodo GET

servicio2_blueprint.add_url_rule("/locations", view_func=get_locations, methods=["GET"])

servicio2_blueprint.add_url_rule(
    "/characters", view_func=get_characters, methods=["GET"]
)

servicio2_blueprint.add_url_rule("/episodes", view_func=get_episodes, methods=["GET"])

servicio2_blueprint.add_url_rule(
    "/character_episodes", view_func=get_character_episodes, methods=["GET"]
)

# metodo POST

servicio2_blueprint.add_url_rule("/locations", view_func=add_location, methods=["POST"])

servicio2_blueprint.add_url_rule(
    "/characters", view_func=add_character, methods=["POST"]
)

servicio2_blueprint.add_url_rule("/episodes", view_func=add_episode, methods=["POST"])

servicio2_blueprint.add_url_rule(
    "/character_episodes", view_func=add_character_episode, methods=["POST"]
)

# metodo PUT

servicio2_blueprint.add_url_rule(
    "/locations/<int:location_id>", view_func=edit_location, methods=["PUT"]
)

servicio2_blueprint.add_url_rule(
    "/characters/<int:character_id>", view_func=edit_character, methods=["PUT"]
)

servicio2_blueprint.add_url_rule(
    "/episodes/<int:episode_id>", view_func=edit_episode, methods=["PUT"]
)

servicio2_blueprint.add_url_rule(
    "/character_episodes/<int:character_id>/<int:episode_id>",
    view_func=edit_character_episode,
    methods=["PUT"],
)
