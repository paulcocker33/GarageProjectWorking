from django.shortcuts import render
from django.http import Http404
from itertools import chain
from .models import Garage_User, Door_Controller, Controller_Type

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, this is the default interface.")

def users(request):
    user_list = Garage_User.objects.order_by('id')
    context = {'latest_user_list':user_list}
    return render(request,'GarageControllerApp/users.html', context)

def specific_user(request, user_id):
    user_list = Garage_User.objects.filter(id = user_id)
    context = {'latest_user_list':user_list}
    return render(request,'GarageControllerApp/users.html', context)

def controllers(request):
    controller_list = Door_Controller.objects.order_by('id')
    context = {'latest_controller_list':controller_list}
    return render(request,'GarageControllerApp/controllers.html', context)

def specific_controller(request, controller_id):
    controller_list = Door_Controller.objects.filter(id = controller_id)
    context = {'latest_controller_list':controller_list}
    return render(request,'GarageControllerApp/controllers.html', context)
