# src/app.py (or your main application file)
from flask import Flask
from src.scripts.servicio1.routes import servicio1_blueprint
from src.scripts.servicio2.routes import servicio2_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(servicio1_blueprint)
app.register_blueprint(servicio2_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
