from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
import random
  # the index function is called when root is visited
def index(request):
    try:
        request.session['gold']
    except KeyError:
        request.session['gold'] = 0
    return render(request, 'index.html')

def process(request, building_type):
    "hit process"
    time = datetime.now().strftime("%Y/%m/%d %I:%M:%S %p")
    gold = 0
    action = 'earned'
    if building_type == 'farm':
        gold = random.randrange(10,20+1)
    elif building_type == 'cave':
        gold = random.randrange(5,10+1)
    elif building_type == 'house':
        gold = random.randrange(2,5+1)
    else:
        gold = random.randrange(-50,50+1)
        if gold < 0:
            action = 'lost'
        else:
            action = 'win'
    activity = {
        'class': action,
        'message': "You {} {} golds from the {} at {}".format(action, gold, building_type, time)
    }
    try:
        activity_list = request.session['activities']
    except KeyError:
        activity_list = []
    request.session['gold'] += gold
    activity_list.append(activity)
    request.session['activities'] = activity_list
    return redirect('/')
