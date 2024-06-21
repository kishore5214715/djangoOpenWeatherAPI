from django.shortcuts import render
import urllib.request
import json


# Create your views here.
def index(request):
    if request.method == 'POST':
        location = request.POST['location']
        api_key='127beeebb56a5d49d94783257c929c01'
        url=f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
        res = urllib.request.urlopen(url).read()
        json_data = json.loads(res)
        data = {
            "location":location,
            "country_code":str(json_data['sys']['country']),
            "longtitude":str(json_data['coord']['lon']),
            "latitude":str(json_data['coord']['lat']),
            "temperature":float(json_data['main']['temp']),
            "humidity":float(json_data['main']['humidity']),
        }
    else:
        data={}

    return render(request, 'index.html',data)