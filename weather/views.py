import requests
from django.shortcuts import render
from .forms import CityForm

def get_weather(request):
    weather_data = None
    error_message = None
    
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = '8557d94d11eba2cf2016ae0aaf0e73f1'  # API key
            url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
            
            try:
                response = requests.get(url)
                response.raise_for_status()
                weather_data = response.json()
            except requests.RequestException:
                error_message = "Failed to fetch weather data. Please try again."
            except ValueError:
                error_message = "Invalid response from weather service."
    else:
        form = CityForm()
    
    return render(request, 'weather/weather.html', {
        'form': form,
        'weather_data': weather_data,
        'error_message': error_message
    }) 