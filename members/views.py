from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def home(request):
    template = loader.get_template('home.htm')
    return HttpResponse(template.render())

def list_members(request):
    members = Member.objects.all().values()
    template = loader.get_template('list_members.htm')

    context = {
        'members': members,
    }

    return HttpResponse(template.render(context, request))

def member_details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('member_details.htm')

    context = {
        'member': member,
    }

    return HttpResponse(template.render(context, request))

def testing(request):
    members = Member.objects.all()
    template = loader.get_template('testing_template.htm')

    context = {
        'members': members,
    }

    return HttpResponse(template.render(context, request))
