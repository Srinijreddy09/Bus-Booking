from django.db import models
from django.contrib.auth.models  import User

# Create your models here.
class Bus(models.Model):
    name=models.CharField(max_length=100)
    number=models.CharField(max_length=100,unique=True)
    origin=models.CharField(max_length=100)
    destination=models.CharField(max_length=100)
    start_time=models.DateTimeField()
    reach_time=models.DateTimeField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    total_seats=models.PositiveBigIntegerField() 
    
    
    def __str__(self):
        return f"{self.name} ({self.number}) - {self.origin} to {self.destination}"
class Seats(models.Model):
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE,related_name='seats')
    seat_number=models.CharField(max_length=10)
    is_booked=models.BooleanField(default=False)
    def __str__(self):
        return f"{self.bus} - Seat {self.seat_number} - {'Booked' if self.is_booked else 'Available'}"
class Booking(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='bookings')
    bus=models.ForeignKey(Bus,on_delete=models.CASCADE,related_name='bookings')
    seat=models.ForeignKey(Seats,on_delete=models.CASCADE,related_name='bookings')
    booking_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Booking by {self.user.username}  -{self.bus.name} - Seat {self.seat.seat_number} - {self.booking_time.strftime('%Y-%m-%d %H:%M:%S')}"