# 📝 Sticky Notes Web Application (Django)

## 📌 Overview
This project is a Django-based Sticky Notes web application that allows users to register, log in, and manage their personal notes. Each user can create, edit, and delete their own notes securely.

---

## 🚀 Features
- 🔐 User Registration & Authentication (Login/Logout)
- 📝 Create, Edit, Delete Notes (CRUD Operations)
- 🎨 Colorful Sticky Notes (Custom Color Picker)
- 📌 Pin Important Notes (appear at top)
- 🔍 Search Notes (by title or content)
- 🌙 Dark Mode Toggle
- 👤 User-specific notes (no data leakage)
- 🎨 Modern UI using Bootstrap

---

## 🛠️ Technologies Used
- **Backend:** Django (Python)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Authentication:** Django built-in auth system

---

## 📂 Project Structure
```
sticky_notes_project/
│
├── manage.py
├── sticky_project/
│   ├── settings.py
│   ├── urls.py
│
├── notes/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│
├── db.sqlite3
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```
git clone https://github.com/Mohsan-R/sticky-notes-django.git
cd sticky-notes-django
```

---

### 2️⃣ Create Virtual Environment
```
python -m venv venv
venv\Scripts\activate
```

---

### 3️⃣ Install Dependencies
```
pip install django
```

---

### 4️⃣ Apply Migrations
```
python manage.py makemigrations
python manage.py migrate
```

---

### 5️⃣ Run the Server
```
python manage.py runserver
```

---

### 6️⃣ Open in Browser
```
http://127.0.0.1:8000/login/
```

---

## 🔐 Authentication Flow
- New users must **register first**
- Then **login** to access notes
- All note operations are protected using `login_required`
- Each user can only access their own notes

---

## 🎯 Key Concepts Used
- Django Models (Database Design)
- Django ModelForms
- Function-Based Views
- URL Routing
- Template Inheritance
- Authentication System
- CRUD Operations

---

## 💡 Extra Features (Bonus)
- Color picker input for notes
- Search functionality
- Pin important notes
- Dark mode UI
- Bootstrap styling for modern interface

---

## 👨‍💻 Author
**Mohsan Raza**  


---


