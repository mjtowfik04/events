from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate, logout
from user.forms import LoginForm

from user.forms import CustomRegistrationForm

# Create your views here.


def sign_up(request):
    form = CustomRegistrationForm()
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign-in')
        else:
            print("Form is not valid")
    return render(request, 'registration/register.html', {"form": form})


def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            print("Form errors:", form.errors)  
    return render(request, 'registration/login.html', {'form': form})

def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('sign-in')