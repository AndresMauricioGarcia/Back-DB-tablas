
from flask import Flask
from src.scripts.servicio1.routes import pokemon_blueprint
from src.scripts.servicio2.routes import rick_and_morty_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(pokemon_blueprint)
app.register_blueprint(rick_and_morty_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
