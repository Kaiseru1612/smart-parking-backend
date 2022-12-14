from xml.etree.ElementInclude import include
from django.contrib import admin
from django.db import router
from django.urls import path, include
# from parking_api.views import ParkingLotViewset
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from profiles_api import views as user_views
from parking_lot import views as parking_views
from booking import views as booking_views

schema_view = get_schema_view(
   openapi.Info(
      title="Spark API",
      default_version='v1',
      description="This is a smart parking api",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router=DefaultRouter()

router.register('profile', user_views.UserProfileViewSet)
router.register('feed', user_views.UserProfileFeedViewSet)
router.register('parking-lot', parking_views.ParkingLotViewset)
router.register('corner', parking_views.CornerViewset)
router.register('bookings', booking_views.BookingViewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]