from flask import Flask
from flask_cors import CORS
from config import config
from routes import Usuario, Opciones

app = Flask(__name__)


def page_not_found(error):
    return "<h1>Página no encontrada. </h1>", 404

CORS(app)

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(Usuario.main, url_prefix='/api/usuarios')
    app.register_blueprint(Opciones.main, url_prefix='/api/opciones')

    #Error handler
    app.register_error_handler(404, page_not_found)
    app.run()
