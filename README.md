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
[   ```bash
   git clone https://github.com/yourname/django-jobboard.git
   cd django-jobboard](https://github.com/abdullahfayyaz/Django-JobBoard-App.git
)
