from django.shortcuts import render, HttpResponse, redirect
# Create your views here.
from time import strftime
import random

def index(request):
    return render(request, 'index.html')

def process_money(request):
    if 'count' in request.session:
        if request.POST['building'] == 'farm':
            score = random.randint(10,20)
        elif request.POST['building'] == 'cave':
            score = random.randint(5,10)
        elif request.POST['building'] == 'house':
            score = random.randint(2,5)
        elif request.POST['building'] == 'casino':
            score = random.randint(-50,50)
        request.session['count'] += score
        if score > 0:
            request.session['box'].insert(0,{'class': 'green', 'log': f"Haz ganado  {score} puntos oro de la {request.POST['building']}! {strftime('%Y/%m/%d %I:%M:%S %p')}"})
        else:
            request.session['box'].insert(0,{'class': 'red', 'log': f"Haz perdido {-1*score} golds at the {request.POST['building']}... Ouch!!! {strftime('%Y/%m/%d %I:%M:%S %p')}"})
    else:
        request.session['count'] = 0
        request.session['box'] = []
    return redirect('/')

def reset(request):
    request.session['count'] = 0
    request.session['box'] = []
    return redirect('/')

