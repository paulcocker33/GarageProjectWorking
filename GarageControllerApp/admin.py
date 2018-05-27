from django.contrib import admin
from .models import Garage_User, Door_Controller, Controller_Type

# Register your models here
admin.site.register(Garage_User),
admin.site.register(Door_Controller),
admin.site.register(Controller_Type),
