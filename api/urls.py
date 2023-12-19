from django.urls import path

from .views import ProfileAPI


urlpatterns = [
    path("prof/<int:user_id>/", ProfileAPI.as_view(), name="prof"),
]