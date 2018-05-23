from django.contrib import admin
from .models import Appointment


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'barber_name', 'time']

admin.site.register(Appointment, AppointmentAdmin)
