from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def ruturaj(request):
    return HttpResponse('<h1>Ruturaj is new Captain of CSK</h1>')