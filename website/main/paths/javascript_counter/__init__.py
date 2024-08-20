from .views import javascript_counter
from .views import index
from flask import Flask

def create_app():

    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    app.register_blueprint(javascript_counter)
    
    return app

if __name__ == "__main__":
    create_app()