from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'

    db.init_app(app)

    from app.routes.main_routes import main
    app.register_blueprint(main)

    from app.routes.employee_routes import employee_bp
    app.register_blueprint(employee_bp)

    return app
