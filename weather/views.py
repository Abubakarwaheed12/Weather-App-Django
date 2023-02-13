from django.shortcuts import render ,redirect
import requests
# Create your views here.
def home(request):
    try:
        if request.method=='POST':
            city=request.POST.get('city')
            url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
            r=requests.get(url.format(city)).json()
            print(r) 

            city_weahter={
                'city':city,
                'temprature':r['main']['temp'],
                'description':r['weather'][0]['description'],
                'icon':r['weather'][0]['icon'],
            }

            print(city_weahter) 
            context={
            'city_weather':city_weahter,
             }
            return render(request, 'index.html' ,context)

    except Exception as e :
        print(e)
    return render(request, 'index.html' )
