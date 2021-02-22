from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from .forms import LoginForm
import datetime

def login_view(request):
    form = LoginForm(request.POST or None)

    context = {
        'form': form,
    }

    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data. get('password')

        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('home')
        else:
            request.session['invalid_user'] = 1
        
    return render(request, 'users/login.html', context)
    

def logout_view(request):
    logout(request, user)