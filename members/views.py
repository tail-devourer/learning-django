from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def list_members(request):
    template = loader.get_template('list_members.htm')
    return HttpResponse(template.render())
