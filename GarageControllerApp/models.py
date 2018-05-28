from django.db import models


# Create your models here.
class Controller_Type(models.Model):
    name = models.CharField(max_length=30)
    device_path = models.TextField()
    def __str__(self):
        return self.name

class Door_Controller(models.Model):
    name = models.TextField(blank=False)
    number = models.TextField(blank=True, null=True)
    street = models.TextField(blank=True, null=True)
    locality = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    uniqueID = models.CharField(max_length=20,blank=False, null=False)
    device_Online = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add = True)
    ip_address = models.TextField()
    device_port = models.IntegerField()
    controller_type = models.ForeignKey(Controller_Type, on_delete=models.CASCADE, related_name='owner')
    def __str__(self):
        return self.name


class Garage_User(models.Model):
    first_name = models.CharField(max_length=30, null=True)
    middle_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email_address = models.TextField(blank=False, null=False)
    phone_number = models.CharField(max_length=20, null=True)
    password = models.CharField(max_length=20,blank=False, null=False)
    registered_devices = models.ForeignKey(Door_Controller, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

