# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect


def index(request):
    if 'words' in request.session:
        context = {'words': request.session['words']}
        return render (request, 'session_form/index.html', context)
    else:
        request.session['words'] = []
        return render(request, 'session_form/index.html')

def add_word(request):
    if "font" not in request.POST:
        font = None
    else:
        font = request.POST['font']
    entry = {"word": request.POST['word'],
            "color": request.POST['color'],
            "font": font,'time':strftime("%A %B %d, %Y\n%H:%M %p", gmtime())}
    words = request.session['words']
    words.append(entry)
    request.session['words'] = words
    return redirect('/')

def clear(request):
    del request.session['words']
    return redirect('/')
