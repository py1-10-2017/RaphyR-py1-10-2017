from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited
def index(request):
    return render(request, 'index.html')

def process(request):
    print request.POST['name']
    print request.POST['location']
    print request.POST['language']
    return redirect('/result')

def result(request):
    print "hit result!"
    return render(request, 'result.html')
