from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import post_city
from .views import list_of_cities

app_name = 'city_collector'

urlpatterns = [
                  path('city/', post_city, name='city'),
                  path('list_of_cities/', list_of_cities, name='list_of_cities')
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
