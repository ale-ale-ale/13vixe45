from django.shortcuts import render, redirect

from rest_framework.generics import ListAPIView

from .forms import CityFormset
from .models import SomeCity
from .serializers import CitySerializer


def post_city(request):
    if request.method == 'POST':
        formset = CityFormset(request.POST)
        if formset.is_valid():
            for form in formset:
                city = form.cleaned_data.get('city')
                if city:
                    SomeCity(city=city).save()
            return redirect('/thanks/')
    else:
        formset = CityFormset()

    return render(request, 'city_collector/form.html', {'formset': formset})


def thanks(request):
    return render(request, template_name='city_collector/thanks.html')


class ListOfCities(ListAPIView):
    serializer_class = CitySerializer
    queryset = SomeCity.objects.all()
