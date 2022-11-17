import requests
from django.shortcuts import render


def covid19_API(n):
    URL = 'http://openapi.seoul.go.kr:8088/547171685163686f35324270474f6e/json/TbCorona19CountStatus/1/'+str(n)+'/'
    API = requests.get(URL).json()
    data = API['TbCorona19CountStatus']['row']
    return data


def home(request):
    value = covid19_API(1)[0]
    return render(request, 'home.html', {'value': value})
