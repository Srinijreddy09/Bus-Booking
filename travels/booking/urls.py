from django.urls import path
from . import views
from .views import RegisterView, LoginView, BookingView, UserBookingsView

urlpatterns = [
    path('buses/', views.BusCreateListView.as_view(), name='bus-list-create'),
    path('register/', RegisterView.as_view(), name='user-registration'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('user-bookings/<int:user_id>/', UserBookingsView.as_view(), name='user-bookings'),
    path('booking/', BookingView.as_view(), name='booking'),
]
