from django.shortcuts import render
from django.http import HttpResponse

def list_members(request):
    return HttpResponse("Hello, World!")
