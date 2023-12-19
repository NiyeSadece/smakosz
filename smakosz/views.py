import requests
import json
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Profile, Table, Reservation


@login_required()
def reservation_confirmed(request):
    return render(request, 'smakosz/reservation_confirmed.html')


class ReservationView(LoginRequiredMixin, FormView):
    """"Using FormView instead of Model View to a little minimalise getting too much into Django logic
    and to avoid changes in models AGAIN"""
    template_name = "smakosz/reservation_form.html"
    form_class = ReservationForm
    success_url = "/smakosz/reservation_confirmed/"

    def form_valid(self, form):
        """This part is unnecessarily extra, but I've written we're using Django REST Framework, so we're using it ¯\_(ツ)_/¯"""
        try:
            username = self.request.user
            user = User.objects.get(username=username)
            user_id = user.id
            profile_response = requests.get(f"http://127.0.0.1:8000/api/prof/{user_id}/") # should declare DOMAIN var in .env to be proper but eh
            data = json.loads(profile_response.text)
            profile_id = data["id"]
            form = form.cleaned_data
            profile = Profile.objects.get(pk=profile_id)
            date = form["date"]
            table = Table.objects.get(pk=form["table"].id)
            how_many = form["how_many"]
            reservation = Reservation(customer=profile, table=table, date=date, how_many=how_many)
            reservation.save()
            return super().form_valid(form)
        except:
            messages.error(self.request, "Musisz uzupełnić profil, by zarezerwować stolik")
            return redirect("users-profile")


class HomeView(ListView):
    model = Reservation
    paginate_by = 10
    template_name = 'home.html'

    def get_queryset(self):
        try:
            username = self.request.user
            user = User.objects.get(username=username)
            user_id = user.id
            profile_response = requests.get(
                f"http://127.0.0.1:8000/api/prof/{user_id}/")  # should declare DOMAIN var in .env to be proper but eh
            data = json.loads(profile_response.text)
            profile_id = data["id"]
            profile = Profile.objects.get(pk=profile_id)
            return Reservation.objects.filter(customer=profile)
        except:
            return None
