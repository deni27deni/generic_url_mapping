from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def virat(request):
    return HttpResponse('<h1>This year King Kohli defintely lift the Trophy for RCB</h1>')