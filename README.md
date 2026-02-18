# STUDENT-MANAGEMENT-SYSTEM-_-HYRUP
Secure Student Management System built with Django REST Framework featuring JWT authentication, role-based authorization, pagination, search, and Swagger documentation.
# HYRUP – Student Management System (Backend)

## 📋 Overview
A secure, production-ready RESTful Student Management System built with Django and Django REST Framework. The system implements JWT authentication, role-based authorization, and comprehensive student profile management with advanced query features.

## 🚀 Features

### Core Functionality
- **Secure Authentication**: JWT-based with access/refresh tokens
- **Role-Based Access**: Admin and Student roles with different permissions
- **Student Management**: Complete CRUD operations with soft delete
- **Advanced Queries**: Search, pagination, and ordering support
- **API Documentation**: Interactive Swagger UI

### Security Implementation
- Email-based custom user model (no username)
- Passwords hashed with PBKDF2
- JWT tokens with short expiration (15 min access, 7 days refresh)
- Token rotation and blacklisting enabled
- Rate limiting on auth endpoints
- All endpoints protected by default

## 🛠️ Tech Stack
- **Backend**: Python 3.13, Django 5.0
- **API Framework**: Django REST Framework
- **Authentication**: SimpleJWT
- **Database**: SQLite (development)
- **Documentation**: drf-spectacular (Swagger)
- **Version Control**: Git

## 📊 Database Model

### Student Model
| Field | Type | Description |
|-------|------|-------------|
| `student_id` | String | Unique identifier |
| `first_name` | String | Student first name |
| `last_name` | String | Student last name |
| `user` | OneToOne | Linked User account |
| `course` | String | Enrolled course |
| `year` | Integer | Current year |
| `gpa` | Decimal | 0-10 scale |
| `credits_earned` | Integer | Total credits |
| `status` | Choice | active/graduated/dropped |
| `phone` | String | Contact number |
| `address` | Text | Physical address |
| `is_deleted` | Boolean | Soft delete flag |
| `created_at` | DateTime | Timestamp |
| `updated_at` | DateTime | Last update |

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/v1/auth/register/` | Register new user |
| POST | `/api/v1/auth/login/` | Login & receive tokens |
| POST | `/api/v1/auth/refresh/` | Refresh access token |

### Student Management
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/v1/students/` | List students (paginated) |
| POST | `/api/v1/students/` | Create student |
| GET | `/api/v1/students/{id}/` | Retrieve student |
| PUT | `/api/v1/students/{id}/` | Update student |
| DELETE | `/api/v1/students/{id}/` | Soft delete student |

### Query Parameters

## 👥 Role-Based Access

### Admin Privileges
- View all student records
- Create new students
- Update any student
- Soft delete students

### Student Privileges
- View only own profile
- No delete permissions
- Read-only access

## 📦 Installation

### Prerequisites
- Python 3.13+
- Git
- Virtual environment (recommended)

### Setup Instructions

1. **Clone Repository**
   ```bash
   git clone https://github.com/mithune27/STUDENT-MANAGEMENT-SYSTEM.git
   cd STUDENT-MANAGEMENT-SYSTEM
   # Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt

cp .env.example .env
# Edit .env with your settings:
# SECRET_KEY=your-secret-key
# DEBUG=True
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
API Base: http://127.0.0.1:8000/api/v1/
Admin: http://127.0.0.1:8000/admin/
Documentation: http://127.0.0.1:8000/api/docs/

SECRET_KEY=your-secret-key-here
DEBUG=True
JWT_ACCESS_TOKEN_LIFETIME=15  # minutes
JWT_REFRESH_TOKEN_LIFETIME=7   # days
