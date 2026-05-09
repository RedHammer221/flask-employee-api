# flask-employee-api
A backend CRUD API for managing employee records built with Flask and SQLite.

# Employee Management System

A backend CRUD API for managing employee records built with Flask and SQLite.

## Features

- Create employees
- View all employees
- View single employee
- Update employee data
- Delete employees
- REST API architecture
- SQLite database integration
- SQLAlchemy ORM

---

## Technologies Used

- Python
- Flask
- SQLite
- SQLAlchemy

---

## Project Structure

backend/
│
├── app/
│   ├── models/
│   ├── routes/
│   └── static/
│
├── run.py
└── create_db.py

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /employees | Get all employees |
| GET | /employees/<id> | Get single employee |
| POST | /employees | Create employee |
| PUT | /employees/<id> | Update employee |
| DELETE | /employees/<id> | Delete employee |

---

## Installation

Clone repository:

```bash
git clone https://github.com/YOUR_USERNAME/employee-management-system.git
```

Create virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run database setup:

```bash
python create_db.py
```

Run server:

```bash
python run.py
```

---

## Future Improvements

- Authentication system
- Image uploads
- Search and filtering
- Pagination
- React frontend
- Docker deployment

---
