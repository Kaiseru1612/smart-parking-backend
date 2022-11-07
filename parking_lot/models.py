from unicodedata import decimal
import uuid
from django.db import models
# from django.contrib.gis.geos import Point
# from django.contrib.gis.db import models as polimodels

# Create your models here.


class Corner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # longtitude = models.FloatField(default=0)
    # lattitude = models.FloatField(default=0)
    longtitude = models.FloatField(default=0)
    lattitude = models.FloatField(default=0)
    

class ParkingLot(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    total_space = models.DecimalField(max_digits=3, decimal_places=0)
    occopied_space = models.DecimalField(max_digits=3, decimal_places=0)
    price = models.DecimalField(max_digits=7, decimal_places=0)
    area = models.ManyToManyField(Corner)
    date_created=models.DateTimeField(auto_now_add=True)



    
    def __str__(self):
        """Return the model as a id"""
        return self.id




