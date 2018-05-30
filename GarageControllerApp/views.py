from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from datetime import datetime
from ipware import get_client_ip

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
    controller.device_Online=1
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
        return render(request, 'GarageControllerApp/nothing_found.html')
