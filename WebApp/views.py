from django.shortcuts import render

def index(req):
    return render(req, 'index.html')
# Create your views here.
