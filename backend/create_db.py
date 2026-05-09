from app import create_app, db
from app.models.employee import Employee

app = create_app()

with app.app_context():
    db.create_all()
    print("Database created!")
