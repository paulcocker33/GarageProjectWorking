from django.shortcuts import render
from django.http import Http404
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .models import Garage_User, Door_Controller, Controller_Type
from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'new_user.html', {'form': form})


def users(request):
    user_list = Garage_User.objects.order_by('id')
    context = {'latest_user_list': user_list}
    return render(request, 'GarageControllerApp/users.html', context)


def specific_user(request, user_id):
    user_list = Garage_User.objects.filter(id=user_id)
    context = {'latest_user_list': user_list}
    return render(request, 'GarageControllerApp/users.html', context)


def controllers(request):
    controller_list = Door_Controller.objects.order_by('id')
    context = {'latest_controller_list': controller_list}
    return render(request, 'GarageControllerApp/controllers.html', context)


def specific_controller(request, controller_id):
    controller_list = Door_Controller.objects.filter(id=controller_id)
    context = {'latest_controller_list': controller_list}
    return render(request, 'GarageControllerApp/controllers.html', context)


def index(request):
    return render(request, 'GarageControllerApp/welcome.html')
