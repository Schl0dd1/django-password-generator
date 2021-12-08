from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def home(request): 
    return render(request, 'generator/home.html')

def generatedpassword(request):
    
    length = int(request.GET.get('length'))

    characters = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        characters.extend([x.upper() for x in characters])
    if request.GET.get('numbers'):
        characters.extend(list((str(x) for x in range(10))))
    if request.GET.get('specialcharacters'):
        characters.extend(list('#*!?$§_()'))

    thepassword = '' 
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/generatedpassword.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')