from django.shortcuts import render

from django.shortcuts import render
import json
import urllib.request


def index(request):
	if request.method == 'POST':
		city = request.POST['city']

		source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=509fd6d3ff920372de7b25c8d35f8057'.format(city.replace(" ",""))).read()
	
		list_of_data = json.loads(source)

		data = {
			"city_name": city,
			"country_code": str(list_of_data['sys']['country']),
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']),
			"temp": str(list_of_data['main']['temp']) + 'k',
			"pressure": str(list_of_data['main']['pressure']),
			"humidity": str(list_of_data['main']['humidity']),
		}
	else:
		data ={}
	return render(request, "index.html", data)
