from flask import Flask
from flask_cors import CORS
from config import config
from routes import Usuario

app = Flask(__name__)


def page_not_found(error):
    return "<h1>Página no encontrada. </h1>", 404

CORS(app, resources= {"origins": "http://localhost:9300"}})

if __name__ == '__main__':
    app.config.from_object(config['development'])

    #Blueprints
    app.register_blueprint(Usuario.main, url_prefix='/api/usuarios')

    #Error handler
    app.register_error_handler(404, page_not_found)
    app.run()
