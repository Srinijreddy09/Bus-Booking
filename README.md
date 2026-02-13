# 🚌 Bus Ticket Booking Application (Django REST Framework)

A RESTful backend application for booking bus tickets, built using **Django** and **Django REST Framework (DRF)**.  
This system allows users to register, log in securely, browse buses, check seat availability, and book tickets in real time.

---

## 📌 Project Overview

The Bus Ticket Booking Application provides a scalable backend solution for managing transportation bookings.

👤 Users can:

- Register an account  
- Log in securely  
- Browse available buses  
- Check seat availability  
- Book seats  
- View their bookings  

🛠️ Administrators can manage buses, routes, timings, seats, and bookings through the Django Admin Panel.

---

## 🚀 Features

### 👤 User Features

- ✅ User Registration  
- 🔐 Secure Login (Token Authentication)  
- 🚌 View Available Buses  
- 📄 View Bus Details  
- 💺 Check Seat Availability  
- 🎟️ Book Seats in Real Time  
- 📖 View Booking History  

---

### 🔐 Authentication & Security

- Token-based authentication using DRF  
- Protected API endpoints  
- Permission control using `IsAuthenticated`  
- Secure access via request headers  

---

### 🛠️ Admin Features

Managed through Django Admin Dashboard:

- 🛣️ Manage Buses  
- 📍 Manage Routes (Origin & Destination)  
- ⏰ Manage Schedules & Timings  
- 💺 Monitor Seat Availability  
- 📖 Manage Bookings  
- 👥 View Registered Users  

---

## 🏗️ Tech Stack

- **Backend:** Python, Django  
- **API Framework:** Django REST Framework (DRF)  
- **Database:** SQLite  
- **Authentication:** DRF Token Authentication  
- **Admin Panel:** Django Admin  

---

## 📂 Project Structure

Bus-Booking/
│
├── booking/
│ ├── models.py
│ ├── serializers.py
│ ├── views.py
│ ├── urls.py
│
├── travels/
│ ├── settings.py
│ ├── urls.py
│
├── manage.py
└── README.md


---

## ⚙️ Setup & Installation

### 1️⃣ Clone the Repository

bash
git clone https://github.com/Srinijreddy09/Bus-Booking.git
cd Bus-Booking
2️⃣ Create Virtual Environment
python -m venv env
Activate environment:

Windows

env\Scripts\activate
Mac/Linux

source env/bin/activate
3️⃣ Install Dependencies
If requirements file exists:

pip install -r requirements.txt
Otherwise:

pip install django djangorestframework
4️⃣ Apply Migrations
python manage.py makemigrations
python manage.py migrate
5️⃣ Create Superuser
python manage.py createsuperuser
6️⃣ Run the Server
python manage.py runserver
🔗 API Endpoints
Method	Endpoint	Description
POST	/register/	Register a new user
POST	/login/	Login and get auth token
GET	/buses/	List all buses
GET	/buses/<id>/	Get bus details
POST	/booking/	Book seats
GET	/user-bookings/<user_id>/	View user bookings
🔒 Authentication Example
Include the token in request headers:

Authorization: Token your_token_here
🧠 Learning Outcomes
This project demonstrates:

REST API development using DRF

Token-based authentication

Model relationships using ForeignKey

CRUD operations

Django Admin usage

Real-time seat booking logic

Secure backend design

🎯 Future Enhancements
💳 Online payment integration

📧 Email/SMS booking confirmation

🪑 Seat selection interface

🌐 Frontend integration (React/Angular)

🗄️ PostgreSQL database support

☁️ Deployment on AWS/Heroku

👨‍💻 Author
Srinij Reddy Musku
B.Tech CSE (Data Science)
Frontend Developer | Python Enthusiast
