from src.settings import application
from src.scripts.servicio1.routes import servicio1_blueprint
from src.scripts.servicio2.routes import servicio2_blueprint



# Register blueprints
application.register_blueprint(servicio1_blueprint)
application.register_blueprint(servicio2_blueprint)

if __name__ == "__main__":
    application.run(debug=True)

