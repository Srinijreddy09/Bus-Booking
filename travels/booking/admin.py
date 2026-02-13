from django.contrib import admin

# Register your models here.

from .models import Bus,Seats
class BusAdmin(admin.ModelAdmin):
    list_display = ('name', 'number', 'origin', 'destination', 'start_time', 'reach_time', 'price', 'total_seats', )
    search_fields = ('name', 'number', 'origin', 'destination')
    list_filter = ('origin', 'destination')
class SeatsAdmin(admin.ModelAdmin):
    list_display = ('bus', 'seat_number', 'is_booked')
    search_fields = ('bus__name', 'seat_number')
    list_filter = ('is_booked',)
admin.site.register(Bus, BusAdmin)
admin.site.register(Seats, SeatsAdmin)