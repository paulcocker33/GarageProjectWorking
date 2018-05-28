from django.shortcuts import render
from django.http import Http404
from .models import Garage_User, Door_Controller, Controller_Type

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, this is the default interface.")

def index(request):
    user_list = Garage_User.objects.order_by('id')
    context = {'latest_user_list':user_list}
    return render(request,'GarageControllerApp/index.html', context)
