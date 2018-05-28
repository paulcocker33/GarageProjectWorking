from django.urls import path
from . import views

urlpatterns = [
    #all users
    path('users/', views.users, name='index'),
    #specific users
    path('users/<int:user_id>/', views.specific_user, name='specific_user'),
    #all controllers
    path('controllers/', views.controllers, name='controllers'),
    #specific controllers
    path('controllers/<int:controller_id>/', views.specific_controller, name='specific_controller'),
]
