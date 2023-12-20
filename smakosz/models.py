from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    """Technically, Profile model should be in accounts to maintain proper separation,
    but database was done at the very beginning, and now it would mess up with imports."""
    CUSTOMER = "1"
    STAFF = "2"
    ADMIN = "3"
    ROLE_CHOICES = [
        (CUSTOMER, "Customer"),
        (STAFF, "Staff"),
        (ADMIN, "Administrator"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE) # this expands default User model used by Django auth
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=9)
    image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    role = models.CharField(max_length=1, choices=ROLE_CHOICES, default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def save(self, *args, **kwargs):
        """Function to change user's avatar to max 100 x 100"""
        super().save()

        img = Image.open(self.image.path)

        if img.height > 100 or img.width > 100:
            new_img = (100, 100)
            img.thumbnail(new_img)
            img.save(self.image.path)


class Restaurant(models.Model):
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"Restauracja - {self.id}"


class Table(models.Model):
    capacity = models.CharField(max_length=2)
    is_occupied = models.BooleanField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    def __str__(self):
        if int(self.capacity) < 5:
            return f"Stolik {self.id} - {self.capacity} miejsca"
        else:
            return f"Stolik {self.id} - {self.capacity} miejsc"


class Reservation(models.Model):
    customer = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField()
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    how_many = models.CharField(max_length=2)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Rezerwacja na stolik nr {self.table.id} na {self.date} od {self.customer.first_name} {self.customer.last_name}"

