from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    CUSTOMER = 1
    STAFF = 2
    ADMIN = 3
    ROLE_CHOICES = [
        (CUSTOMER, "Customer"),
        (STAFF, "Staff"),
        (ADMIN, "Administrator"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.IntegerField(max_length=9)
    image = models.ImageField()
    role = models.IntegerField(max_length=1, choices=ROLE_CHOICES, default=1)


class Restaurant(models.Model):
    address = models.CharField(max_length=255)


class Table(models.Model):
    capacity = models.IntegerField(max_length=2)
    is_occupied = models.BooleanField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class Reservation(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    how_many = models.IntegerField(max_length=2)
    is_confirmed = models.BooleanField(default=False)

