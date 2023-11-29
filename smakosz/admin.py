from django.contrib import admin
from .models import Profile, Restaurant, Table, Reservation


admin.site.register(Profile)
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Reservation)
