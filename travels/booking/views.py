from django.shortcuts import render
from django.contrib.auth import authenticate, login
from rest_framework.permissions import IsAuthenticated

from rest_framework.authtoken.models import Token
# Create your views here.
#authicatication,permissions,tokens,status,response,
from rest_framework import status,generics
from rest_framework.views import APIView
from .models import Booking, Booking, Bus, Seats
from .serializers import BookingSerializer, UserRegistrationSerializer,BusSerializer,SeatsSerializer

from rest_framework.response import Response

class RegisterView(APIView):
    def post(self,request):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token,created=Token.objects.get_or_create(user=user)
            return Response({'token':token.key},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class LoginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            token,created=Token.objects.get_or_create(user=user)
            return Response({'token':token.key},status=status.HTTP_200_OK)
        return Response({'error':'Invalid credentials'},status=status.HTTP_401_UNAUTHORIZED)
class BusCreateListView(generics.ListCreateAPIView):
    queryset=Bus.objects.all()
    serializer_class=BusSerializer
  
class BusDetailView(generics.RetrieveAPIView):
    queryset=Bus.objects.all()
    serializer_class=BusSerializer
  
class BookingView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        bus_id=request.data.get('bus_id')
        seat_number=request.data.get('seat_number')
        try:
            bus=Bus.objects.get(id=bus_id)
            seat=bus.seats.get(seat_number=seat_number)
            if seat.is_booked:
                return Response({'error':'Seat already booked'},status=status.HTTP_400_BAD_REQUEST)
            seat.is_booked=True
            seat.save()
            booking=Booking.objects.create(user=request.user,bus=bus,seat=seat)
            serializer=BookingSerializer(booking)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        except Bus.DoesNotExist:
            return Response({'error':'Bus not found'},status=status.HTTP_404_NOT_FOUND)
        except Seats.DoesNotExist:
            return Response({'error':'Seat not found'},status=status.HTTP_404_NOT_FOUND)
class UserBookingsView(generics.ListAPIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,user_id):
      if request.user.id!=user_id:
        return Response({'error':'Unauthorized'},status=status.HTTP_401_UNAUTHORIZED)
      bookings=Booking.objects.filter(user_id=user_id)
      serializer=BookingSerializer(bookings,many=True)
      return Response(serializer.data,status=status.HTTP_200_OK)

        
        
