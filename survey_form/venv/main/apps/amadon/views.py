# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

items = [
    {
        "id": 1,
        "name": "Dojo T-Shirt",
        "price": 19.99,
    },
    {
        "id": 2,
        "name": "Dojo Sweater",
        "price": 29.99
    },
    {
        "id": 3,
        "name": "Dojo Cup",
        "price": 4.99
    },
    {
        "id": 4,
        "name": "Algorithm Book",
        "price": 49.99
    }
]

# Create your views here.
def index(req):
    context = {
        "items": items
    }
    return render(req, "index.html", context)

def buy(request, item_id):

    # find item in our items list from the url's item_id matching the 'id' key on the item
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])

    # handle exceptions for session keys if they do not yet exist
    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0

    request.session['total_charged'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_transaction'] = amount_charged
    return redirect('/amadon/checkout')

def checkout(request):
    return render(request, 'checkout.html')
