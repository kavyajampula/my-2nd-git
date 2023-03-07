from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Navya(request):
    return HttpResponse('Navya and Ramya are best friends')

def Ramya(request):
    return HttpResponse('<h1><marquee>Ramya is an intelligent girl</h1></marquee>')   
def Kavya(request):
    return HttpResponse('<h1><marquee>Navya is an intelligent girl</h1></marquee>')    