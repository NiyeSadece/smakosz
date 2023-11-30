from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    how_many = forms.IntegerField(min_value=1, max_value=10)

    class Meta:
        model = Reservation
        fields = ['date', 'how_many', 'table']
        widgets = {
            'date': forms.DateTimeInput(
                format="%Y-%m-%d %H:%M",
                attrs={'type': 'datetime', 'placeholder': 'yyyy-mm-dd HH:MM', 'class': 'form-control'}
            )
        }
