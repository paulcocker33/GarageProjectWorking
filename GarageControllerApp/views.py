from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from datetime import datetime, timedelta
from ipware import get_client_ip
from .forms import Controller_Form
import requests

from .models import Door_Controller, Controller_Type

@login_required
def users(request):
    user_list = User.objects.order_by('id')
    context = {'latest_user_list': user_list}
    return render(request, 'GarageControllerApp/users.html', context)

@login_required
def specific_user(request, user_id):
    user_list = User.objects.filter(id=user_id)
    context = {'latest_user_list': user_list}
    return render(request, 'GarageControllerApp/users.html', context)

@login_required
def controllers(request):
    controller_list = Door_Controller.objects.order_by('id')
    context = {'latest_controller_list': controller_list}
    return render(request, 'GarageControllerApp/controllers.html', context)

@login_required
def specific_controller(request, controller_id):
    controller_list = Door_Controller.objects.filter(id=controller_id)
    context = {'latest_controller_list': controller_list}
    return render(request, 'GarageControllerApp/controllers.html', context)

@login_required
def register_controller(request, controller_uniqueid):
    try:
        controller = Door_Controller.objects.get(uniqueID=controller_uniqueid)
    except Door_Controller.DoesNotExist:
        controller = Door_Controller()
        controller.uniqueID = controller_uniqueid
        controller.create_date = datetime.now()
        controller.controller_type_id = 1
    ip, is_routable = get_client_ip(request)
    controller.ip_address = ip
    controller.device_port = request.GET.get('port')
    controller.device_online = 1
    controller.last_online = datetime.now()
    controller.save()
    context = {'latest_controller_list': [controller]}
    return render(request, 'GarageControllerApp/controllers.html', context)

@login_required
def user_query(request, user_id):
    controller_list = Door_Controller.objects.filter(device_owner=user_id)
    if controller_list.count() > 0:
        context = {'latest_controller_list': controller_list}
        return render(request, 'GarageControllerApp/controllers.html', context)
    else:
        return render(request, 'GarageControllerApp/controllers.html')

@login_required
def add_controller(request):
    if request.method == "POST":
        form = Controller_Form(request.POST)
        if form.is_valid():
            new_controller = Door_Controller()
            new_controller = form.save(commit=False)
            new_controller.create_date = datetime.now()
            new_controller.device_owner = request.user
            ip, is_routable = get_client_ip(request)
            new_controller.ip_address = ip
            new_controller.device_online = 0
            new_controller.device_port = 5000
            new_controller.controller_type_id = 1
            new_controller.save()
            return render(request,'GarageControllerApp/controllers.html', {'controller_list': [new_controller]})
    else:
        form = Controller_Form()
        return render(request, 'GarageControllerApp/register_device.html', {'form': form})

@login_required
def trigger_controller(request, controller_id):
    new_controller = Door_Controller.objects.get(id=controller_id)
    url = 'www.google.com'
    delta = datetime.now() - new_controller.last_online
    if (new_controller.device_Online == 1) & (delta <= 360):
        try:
            r = requests.get(url)
        except requests.exceptions.RequestException as e:
            return render(request,'GarageControllerApp/trigger_fail.html', new_controller, url, e)
    else:
        return render(request, 'GarageControllerApp/trigger_fail.html', {'controller':[new_controller],'url':url,'exception':'controller is not online'})


