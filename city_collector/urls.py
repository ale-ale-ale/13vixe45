from django.urls import path

from .views import post_city, thanks, ListOfCities

app_name = 'city_collector'

urlpatterns = [
    path('city/', post_city, name='city'),
    path('list_of_cities/', ListOfCities.as_view(), name='list_of_cities'),
    path('thanks/', thanks, name='thanks'),
]
