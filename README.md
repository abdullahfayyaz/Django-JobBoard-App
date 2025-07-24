# Django Job Board

A full-featured job board application built with Django. Companies can post jobs; applicants can search, view, and apply. Includes dashboards, file uploads, search filters, and role-based access control.

---

## 🚀 Features

- User registration: company vs applicant roles
- Job CRUD with permissions
- Job listing with search filters (keyword, location, type)
- File upload (resumes)
- Role-specific dashboards
- Best practices: CBVs, ModelForms, security mixins, smart templates

---

## 🧩 Models

- **User** (`AbstractUser`): `is_company`, `is_applicant`
- **Job**: company_name, title, description, company (FK), location, job type, timestamp
- **Application**: job (FK), applicant (FK), resume file, cover letter, timestamp (unique per job-user pair)

---

## 🔧 Setup & Installation

1. Clone this repo:  
https://github.com/abdullahfayyaz/Django-JobBoard-App.git

2. Create virtual environment & install dependencies:
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. Configure MySQL (or any DB) in settings.py:
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'jobboard_db',
    'USER': 'your_user',
    'PASSWORD': 'your_pass',
    'HOST': 'localhost',
    'PORT': '3306',
  }
}

4. Run migrations & create superuser:
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

5. Collect static files and start the server:
python manage.py collectstatic
python manage.py runserver

Navigate to http://127.0.0.1:8000/
