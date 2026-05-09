from app import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    first_name = db.Column(db.String(100), nullable=False)

    last_name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True)

    department = db.Column(db.String(100))

    hire_date = db.Column(db.String(50))

    profile_image = db.Column(db.String(200))
