# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Course
from django.contrib.messages import error
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "index.html", context)

def create(request):
    # errors = User.objects.validate(request.POST)
    # if len(errors):
    #     for field, message in errors.iteritems():
    #         error(request, message, extra_tags=field)
    #
    #     return redirect('/semirestful_users/new')

    Course.objects.create(
        name=request.POST['name'],
        desc=request.POST['description']
    )
    return redirect('/courses')

def confirm(request, course_id):
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'confirm.html', context)

def delete(request, course_id):
    Course.objects.get(id=course_id).delete()
    return redirect('/courses')
