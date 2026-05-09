from flask import Blueprint, jsonify, request, current_app
from app import db
from app.models.employee import Employee
from werkzeug.utils import secure_filename
import os

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
existing_employee = Employee.query.filter_by(
    email=data['email']
).first()

if existing_employee:
    return jsonify({
        "error": "Email already exists"
    }), 400
    
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

# GET SINGLE EMPLOYEE
@employee_bp.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):

    employee = db.session.get(Employee, employee_id)

    if not employee:
        return jsonify({
            "error": "Employee not found"
        }), 404

    return jsonify({
        "id": employee.id,
        "first_name": employee.first_name,
        "last_name": employee.last_name,
        "email": employee.email,
        "department": employee.department
    })

# DELETE EMPLOYEE
@employee_bp.route('/employees/<int:employee_id>', methods=['DELETE'])
def delete_employee(employee_id):

    employee = db.session.get(Employee, employee_id)

    if not employee:
        return jsonify({
            "error": "Employee not found"
        }), 404

    db.session.delete(employee)

    db.session.commit()

    return jsonify({
        "message": "Employee deleted successfully"
    })

# UPDATE EMPLOYEE
@employee_bp.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):

    employee = db.session.get(Employee, employee_id)

    if not employee:
        return jsonify({
            "error": "Employee not found"
        }), 404

    data = request.get_json()

    employee.first_name = data.get(
        'first_name',
        employee.first_name
    )

    employee.last_name = data.get(
        'last_name',
        employee.last_name
    )

    employee.email = data.get(
        'email',
        employee.email
    )

    employee.department = data.get(
        'department',
        employee.department
    )

    db.session.commit()

    return jsonify({
        "message": "Employee updated successfully"
    })

# UPLOAD EMPLOYEE IMAGE
@employee_bp.route(
    '/employees/<int:employee_id>/upload',
    methods=['POST']
)
def upload_employee_image(employee_id):

    employee = db.session.get(Employee, employee_id)

    if not employee:
        return jsonify({
            "error": "Employee not found"
        }), 404

    if 'image' not in request.files:
        return jsonify({
            "error": "No image file provided"
        }), 400

    file = request.files['image']

    if file.filename == '':
        return jsonify({
            "error": "No selected file"
        }), 400

    if not allowed_file(file.filename):
        return jsonify({
            "error": "Invalid file type"
        }), 400

    filename = secure_filename(file.filename)

    filepath = os.path.join(
        current_app.config['UPLOAD_FOLDER'],
        filename
    )

    file.save(filepath)

    employee.profile_image = f"uploads/{filename}"

    db.session.commit()

    return jsonify({
        "message": "Image uploaded successfully",
        "image_path": employee.profile_image
    })
