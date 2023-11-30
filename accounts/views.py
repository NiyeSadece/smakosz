from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from.forms import RegisterForm, UpdateUserForm, UpdateProfileForm


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='users-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'accounts/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
