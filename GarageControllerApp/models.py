from django.db import models


# Create your models here.
class DoorController(models.Model):
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    uniqueID = models.TextField


