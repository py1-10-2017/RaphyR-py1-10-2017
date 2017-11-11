from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
import random
import string
count = 0

def random_word(n):
    allowed_chars = ''.join((string.ascii_letters, string.digits))
    return ''.join(random.choice(allowed_chars) for _ in range(n))

def index(request):
    request.session['count']
    return render(request, "index.html")

def generate(request):
    request.session['count'] += 1
    request.session['word'] = random_word(30)
    return redirect('/')

def reset(request):
    request.session['word'] = "No word generated yet. Please click 'Generate'"
    request.session['count'] = 0
    del request.session['word']
    return redirect('/')
