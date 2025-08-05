from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'recipes/home.html')

def about(request):
    return HttpResponse('Vamos Flamengo!')

def contact(request):
    return HttpResponse('Contact')
