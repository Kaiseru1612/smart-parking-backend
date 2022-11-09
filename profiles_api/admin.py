from django.contrib import admin
from profiles_api import models
from parking_lot.models import Corner

admin.site.register(models.UserProfile)
admin.site.register(models.ProfileFeedItem)
admin.site.register(models.ParkingLot)
admin.site.register(Corner)
