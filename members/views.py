from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Member, Comment
from .forms import CommentForm

def home(request):
    query = request.GET.get('q', '')
    members = None
    form = None

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()

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
        'comments': Comment.objects.all(),
        'form': form,
        'query': query,
    })
