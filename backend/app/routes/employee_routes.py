from flask import Blueprint, jsonify, request

from app import db
from app.models.employee import Employee

employee_bp = Blueprint('employee_bp', __name__)


# GET ALL EMPLOYEES
@employee_bp.route('/employees', methods=['GET'])
def get_employees():

    employees = Employee.query.all()

    result = []

    for employee in employees:
        result.append({
            "id": employee.id,
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "email": employee.email,
            "department": employee.department
        })

    return jsonify(result)


# CREATE EMPLOYEE
@employee_bp.route('/employees', methods=['POST'])
def create_employee():

    data = request.get_json()

    required_fields = ['first_name', 'last_name', 'email']

    for field in required_fields:
        if field not in data:
            return jsonify({
                "error": f"{field} is required"
            }), 400

    new_employee = Employee(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        department=data.get('department')
    )

    db.session.add(new_employee)

    db.session.commit()

    return jsonify({
        "message": "Employee created successfully"
    }), 201
