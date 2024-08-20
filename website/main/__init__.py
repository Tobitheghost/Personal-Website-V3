from flask import Flask
from flask_wtf.csrf import CSRFProtect
from flask_mail import Mail
from .paths.utils.secret import mail_password, mail_username, mail_port, secret_key
from .paths.utils.logging.logs import init_log

init_log()
path_links = []
csrf = CSRFProtect()
mail = Mail()

def create_app():
    
    # Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = secret_key
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    csrf.init_app(app)

    # Email Server
    app.config["MAIL_SERVER"] = "smtp.gmail.com"
    app.config["MAIL_PORT"] = mail_port
    app.config["MAIL_USERNAME"] = mail_username
    app.config["MAIL_PASSWORD"] = mail_password
    app.config["MAIL_USE_TLS"] = False
    app.config["MAIL_USE_SSL"] = True
    mail.init_app(app)

    # Errors
    from .errors import YouGotHigh, weed_error
    app.register_error_handler(YouGotHigh, weed_error)
    
    # BluePrints
    from .views import home
    app.register_blueprint(home)

    from .paths.utils import utilities
    app.register_blueprint(utilities)
    
    from .paths.javascript_counter import javascript_counter
    app.register_blueprint(javascript_counter)

    return app

from main import views

if __name__ == '__main__':
    create_app()