# 🏥 Healthcare Backend API

A Django REST Framework (DRF) based backend system for managing patients, doctors, and their mappings in a healthcare environment. This project includes JWT authentication, CRUD APIs, and PostgreSQL integration.

---

## 📌 Features

- ✅ User Registration & JWT Authentication (Login)
- 🧑‍⚕️ CRUD APIs for Doctors
- 🧑‍🤝‍🧑 CRUD APIs for Patients
- 🔁 Mapping between Patients and Doctors
- 🛡️ Secure endpoints using SimpleJWT
- 🔍 Well-structured Django app with PostgreSQL support

---

## 🛠️ Tech Stack

| Tool            | Description                     |
|-----------------|---------------------------------|
| Python 3.8+     | Backend programming language     |
| Django          | Web framework                    |
| Django REST Framework | REST API toolkit            |
| PostgreSQL      | Relational database              |
| SimpleJWT       | JWT Authentication in DRF        |
| Git + GitHub    | Version control & repository     |
| Postman         | API testing                      |

---

## 🚀 Getting Started (Local Setup)

### 1. Clone the Repository :
git clone https://github.com/Pavan-Kumar401/healthcare-backend.git
cd healthcare-backend

### 2. Create a Virtual Environment : 
python -m venv env
env\Scripts\activate   # For Windows
# OR
source env/bin/activate   # For Mac/Linux

### 3. Install Dependencies :
pip install -r requirements.txt

### 4. Set Up PostgreSQL Database :
Make sure PostgreSQL is installed and running.

Update the DATABASES section in healthcare/settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

### 5. Run Migrations :
python manage.py makemigrations
python manage.py migrate
### 6. Run the Server :
python manage.py runserver
Access the server at: http://127.0.0.1:8000/

🔐 JWT Authentication :
### 1. Register a User :
POST /api/auth/register/

### 2. Login and Get Tokens :
POST /api/auth/login/
Response:
{
  "access": "your_access_token",
  "refresh": "your_refresh_token"
}
### 3. Use Access Token in Headers :
Authorization: Bearer your_access_token

🧪 API Endpoints Overview :
| Endpoint              | Method           | Description             |
| --------------------- | ---------------- | ----------------------- |
| `/api/auth/register/` | POST             | Register new user       |
| `/api/auth/login/`    | POST             | Get JWT tokens          |
| `/api/doctors/`       | GET, POST        | List/Add doctors        |
| `/api/doctors/<id>/`  | GET, PUT, DELETE | Doctor details          |
| `/api/patients/`      | GET, POST        | List/Add patients       |
| `/api/patients/<id>/` | GET, PUT, DELETE | Patient details         |
| `/api/mappings/`      | GET, POST        | Map patients to doctors |

#### 📂 Project Structure :

healthcare_backend/
│
├── healthcare/           # Main Django project
│   ├── settings.py
│   ├── urls.py
│
├── hospital/             # App for doctors & patients
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── serializers.py
│
├── manage.py
├── requirements.txt
├── README.md
└── .gitignore


### 📄 Sample .gitignore
Make sure your .gitignore file includes: 
env/
__pycache__/
*.pyc
db.sqlite3
*.log
*.sqlite3
*.env


🙋‍♂️ Author
### Pavan Kumar
GitHub: @Pavan-Kumar401

### 📬 Feedback or Contributions?
Feel free to open an issue or create a pull request if you'd like to improve this project or suggest enhancements.

### Just say the word!



