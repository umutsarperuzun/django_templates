from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"template_app/first.html")

def weather(request):
    weather_dictionary= {
        "Istanbul" : "30" , 
        "Amsterdam" : "20" ,
        "Tel_Aviv" : "35" ,
        "Paris" : [10,14,20,22] ,
        "London" : {"Morning" : "7" ,"Noon" : "10" , "Afternoon": "12","Night" : "10"}
        }
    return render(request,"template_app/weather.html",context=weather_dictionary)