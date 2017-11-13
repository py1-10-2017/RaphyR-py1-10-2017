# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import HttpResponse, render, redirect

# Create your views here.
def register(req):
    print "users"
    return HttpResponse("'placeholder for users to create a new user record")
    # return render(req, "users/index.html")

def login(req):
    return HttpResponse("placeholder for users to login")

def new(req):
    return redirect('/users')

def all_users(req):
    return HttpResponse("placeholder to later display all the list of users")
