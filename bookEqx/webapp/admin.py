from django.contrib import admin

# Register your models here.

from .models import Room

admin.site.register(Room)


from .models import Reservation

admin.site.register(Reservation)