from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from smakosz.models import Profile


# Maciej Franc
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Dalia Grodzka
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateProfileForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    first_name = forms.CharField(max_length=30,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=30,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    phone_number = forms.CharField(max_length=9,
                                   min_length=9,
                                   required=True,
                                   widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'phone_number']
