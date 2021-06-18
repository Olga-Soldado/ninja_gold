from django.shortcuts import render,redirect
# Create your views here.
from time import strftime
import random

def index(request):
    return render(request, 'index.html')

def process_money(request):
    if 'count' in request.session:
        if request.POST['building'] == 'Granja':
            score = random.randint(10,20)
        elif request.POST['building'] == 'Cueva':
            score = random.randint(5,10)
        elif request.POST['building'] == 'Casa':
            score = random.randint(2,5)
        elif request.POST['building'] == 'Casino':
            score = random.randint(-50,50)
        request.session['count'] += score
        if score > 0:
            request.session['box'].insert(0,{'class': 'green', 'log': f"Haz ganado {score} puntos!. De  {request.POST['building']} {strftime('%Y/%m/%d %I:%M:%S %p')}"})
        else:
            request.session['box'].insert(0,{'class': 'red', 'log': f"Haz perdido {score} puntos !. De {request.POST['building']}{strftime('%Y/%m/%d %I:%M:%S %p')}"})
    else:
        request.session['count'] = 0
        request.session['box'] = []
    return redirect('/')

def reiniciar(request):
    request.session['count'] = 0
    request.session['box'] = []
    return redirect('/')

