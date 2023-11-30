from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.shortcuts import render
from .forms import ReservationForm


@login_required()
def reservation_confirmed(request):
    return render(request, 'smakosz/reservation_confirmed.html')


class ReservationView(LoginRequiredMixin, FormView):
    template_name = "smakosz/reservation_form.html"
    form_class = ReservationForm
    success_url = "/smakosz/reservation_confirmed/"
