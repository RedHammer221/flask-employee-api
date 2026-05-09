from flask import Blueprint, jsonify
from app.models.employee import Employee

employee_bp = Blueprint('employee_bp', __name__)


@employee_bp.route('/employees')
def get_employees():
    employees = Employee.query.all()

    result = []

    for employee in employees:
        result.append({
            "id": employee.id,
            "first_name": employee.first_name,
            "last_name": employee.last_name,
            "email": employee.email
        })

    return jsonify(result)
