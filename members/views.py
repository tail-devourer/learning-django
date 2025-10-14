from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def list_members(request):
    members = Member.objects.all().values()
    template = loader.get_template('list_members.htm')

    context = {
        'members': members,
    }

    return HttpResponse(template.render(context, request))
