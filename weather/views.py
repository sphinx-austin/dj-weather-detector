from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    """
    collect data from the html form
    """
    if request.method == 'POST':
        city = request.POST.get('city')
        # res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'@appid=f47c3ab0eae2e8f11bdbf2be339e4112').read()
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&APPID=f47c3ab0eae2e8f11bdbf2be339e4112').read()
        json_data = json.loads(res)
        data = {
            "country_code" : str(json_data['sys']['country']),
            "coordinate" : str(json_data['coord']['lon']) + ' ' + str(json_data['coord']['lat']),
            "temperature" : str(json_data['main']['temp']) + 'k',
            "pressure" : str(json_data['main']['pressure']),
            "humidity" : str(json_data['main']['humidity']),
        }
    else:
        city = ''
        data = {}

    return render(request, 'weather/index.html', {'city':city, 'data':data})