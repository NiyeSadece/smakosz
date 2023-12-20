"""There were grant plans. These serializers are proof of both dreams and failure."""
from rest_framework import serializers
from django.contrib.auth.models import User
from smakosz.models import Profile, Reservation, Table


# Dalia Grodzka
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
        ]


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = [
            'user',
            'id',
            'first_name',
            'last_name',
            'phone_number',
            'image',
            'role',
        ]


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = [
            'id',
            'capacity',
            'is_occupied',
        ]


class ReservationSerializer(serializers.ModelSerializer):
    customer = ProfileSerializer(read_only=True)
    table = TableSerializer(read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'customer',
            'table',
            'date',
            'how_many',
            'is_confirmed',
        ]
