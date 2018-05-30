from django.urls import path
from . import views

app_name = 'GarageControllerApp'
urlpatterns = [
    #all users
    path('users/', views.users, name='users'),
    #specific users
    path('users/<int:user_id>/', views.specific_user, name='specific_user'),
    #all controllers
    path('controllers/', views.controllers, name='controllers'),
    #specific controllers
    path('controllers/<int:controller_id>/', views.specific_controller, name='specific_controller'),
    #device keepalive
    path('controllers/register/<str:controller_uniqueid>/', views.register_controller, name='register_controller'),
    #user_device_query
    path('userquery/<int:user_id>', views.user_query, name='user_query'),
    #data_entry
    path('register/', views.add_controller, name='add_controller'),
    #trigger a door controller
    path('trigger_controller/<int:controller_id>', views.trigger_controller, name='trigger_controller'),
]