from django.urls import path

from .views import ReservationView, reservation_confirmed


urlpatterns = [
    path("reservation/", ReservationView.as_view(), name="reservation"),
    path('reservation_confirmed/', reservation_confirmed, name='reservation-confirmed'),
]