from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('members', views.list_members, name='list_members'),
    path('members/<slug:slug>', views.member_details, name='member_details'),
]
