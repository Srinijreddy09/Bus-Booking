🚌 Bus Ticket Booking Application (Django REST Framework)
📌 Project Overview

In this project, we built a Bus Ticket Booking Application using Django REST Framework (DRF) for the backend.

This system allows users to:

✅ Register an account

✅ Log in securely

✅ Browse available buses

✅ View seat availability

✅ Book seats in real-time

The Django Admin Panel enables administrators to efficiently manage:

🛣️ Buses

📍 Routes (Origin & Destination)

⏰ Timings

💺 Seat availability

📖 Bookings

The application uses DRF Token Authentication to ensure secure API access and demonstrates how modern web technologies can solve real-world transportation problems efficiently.

🚀 Features
👤 User Features

User Registration

User Login (Token Authentication)

View All Available Buses

View Bus Details

Check Seat Availability

Book Seats

View User Bookings

🔐 Authentication

Token-based Authentication using Django REST Framework

Secure endpoints with permission control (IsAuthenticated)

🛠️ Admin Features

Manage Buses

Manage Seats

Manage Bookings

View Registered Users

Control Routes & Timings

🏗️ Tech Stack

Python

Django

Django REST Framework

SQLite (default DB)

DRF Token Authentication

📂 Project Structure
Bus-Booking/
│
├── booking/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│
├── travels/
│   ├── settings.py
│   ├── urls.py
│
├── manage.py
└── README.md
<img width="655" height="738" alt="image" src="https://github.com/user-attachments/assets/be9253f1-41bc-4b03-952a-b3c9ebfef5d6" />


⚙️ Setup & Installation
1️⃣ Clone the Repository
git clone https://github.com/Srinijreddy09/Bus-Booking.git
cd Bus-Booking

2️⃣ Create Virtual Environment
python -m venv env


Activate environment:

Windows:

env\Scripts\activate


Mac/Linux:

source env/bin/activate

3️⃣ Install Dependencies
pip install -r requirements.txt


If requirements.txt is not available:

pip install django djangorestframework

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create Superuser
python manage.py createsuperuser

6️⃣ Run Server
python manage.py runserver

🔗 API Endpoints
Method	Endpoint	Description
POST	/register/	Register user
POST	/login/	Login user
GET	/buses/	List buses
GET	/buses/<id>/	Bus details
POST	/booking/	Book seat
GET	/user-bookings/<user_id>/	View user bookings
🔒 Authentication Example

Include token in headers:

Authorization: Token your_token_here

🧠 Learning Outcomes

This project demonstrates:

REST API development using DRF

Token-based authentication

Model relationships (ForeignKey)

CRUD operations

Admin dashboard usage

Real-time seat booking logic
