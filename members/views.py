from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def list_members(request):
    members = Member.objects.all()
    template = loader.get_template('list_members.html')

    context = {
        'members': members,
    }

    return HttpResponse(template.render(context, request))

def member_details(request, slug):
    try:
        member = Member.objects.get(slug=slug)
        template = loader.get_template('member_details.html')

        context = {
            'member': member,
        }

        return HttpResponse(template.render(context, request))
    except Member.DoesNotExist:
        template = loader.get_template('404.html')
        return HttpResponse(template.render())
