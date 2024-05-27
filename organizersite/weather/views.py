from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
from django.contrib.auth.decorators import login_required



# Create your views here.
@login_required(login_url='login')
def index(request):
    appid = 'c2101213ea8911d526f0261cc9179964'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + appid

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()     

    cities = City.objects.all()

    all_cities = []

    for city in cities:
        res = requests.get(url.format(city.name)).json()
    city_info = {
        'city': city.name,
        'temp': res["main"]["temp"],
        'icon': res["weather"][0]["icon"]
    }

    all_cities.append(city_info)

    context = {'all_info': all_cities, 'form': form}

    return render (request, 'index.html', context)

