from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json

def get_city(request):
    context = {}
    if request.method == 'POST':
        API_KEY = '<paste your API_KEY here>'
        BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

        city = request.POST['city_name']

        request_url = f'{BASE_URL}?appid={API_KEY}&q={city}&units=metric'
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            print(data)
            longitude = data['coord']['lon']
            latitude = data['coord']['lat']
            country = data['sys']['country']
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            icon = data['weather'][0]['icon']

            context = {'city':str(city).title(), 'weather': str(weather).title(), 'temperature': temp, 'country': country,
             'long': round(longitude, 2), 'lat': round(latitude, 2), 'humidity':humidity, 'wind_speed': wind_speed, 'icon': icon}
        
            google_api_key = ""
            place_url = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400"


        else:
            messages.error(request, 'An error occurred! 1.Did you enter correct city name? 2. Are you connected to the internet? 3. Do you have an API_KEY?')
            return redirect('/')
    return render(request, 'index.html', context)

def acknowledge(request):
    return render(request, 'acknowledgement.html')

