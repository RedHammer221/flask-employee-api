from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    app.config['UPLOAD_FOLDER'] = os.path.join(
        BASE_DIR,
        'static/uploads'
    )

    app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024

    db.init_app(app)

    from app.routes.main_routes import main
    app.register_blueprint(main)

    from app.routes.employee_routes import employee_bp
    app.register_blueprint(employee_bp)

    return app
