from django.db.models import Q
from django.shortcuts import render
from .models import Member

def home(request):
    query = request.GET.get('q', '')
    members = None

    if query:
        members = Member.objects.filter(
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(phone__icontains=query)
        )
    else:
        members = Member.objects.all()

    return render(request, 'list_members.html', {
        'members': members,
        'query': query,
    })
