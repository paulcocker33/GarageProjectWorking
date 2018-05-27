from django.db import models


# Create your models here.
class DoorController(models.Model):
    name = models.TextField(blank=False)
    street = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    uniqueID = models.CharField(max_length=20,blank=False, null=False)
    device_Online = models.BooleanField
    create_date = models.DateTimeField('date added')

class GarageUser(models.Model):
    name = models.TextField()
    email_address = models.TextField(blank=False, null=False)
    password = models.CharField(max_length=20,blank=False, null=False)
    registered_devices= [models.ForeignKey(DoorController, on_delete=models.CASCADE)]
    create_date = models.DateTimeField('date added')
