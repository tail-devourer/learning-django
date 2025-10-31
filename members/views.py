from django.shortcuts import render
from .models import Member

def home(request):
    return render(request, 'list_members.html', {
        'members': Member.objects.all(),
    })
