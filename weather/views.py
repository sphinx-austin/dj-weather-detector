from django.shortcuts import render
import json
import urllib.request

import os

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Create your views here.


def index(request):
    # api_key
    # api_key = os.getenv('API_KEY')
    """
    collect data from the html form
    """
    if request.method == 'POST':
        # fetch city from template
        city = request.POST.get('city')
        # api_key from .env
        api_key = os.getenv('API_KEY')
        # query the api endpoint
        res = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID='+api_key).read()
        json_data = json.loads(res)
        data = {
            "country_code": str(json_data['sys']['country']),
            "coordinate": str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temperature": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data = {}

    return render(request, 'weather/index.html', {'city': city, 'data': data})
