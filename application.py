# src/app.py (or your main application file)
from flask import Flask
from src.scripts.servicio1.routes import pokemon_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(pokemon_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
