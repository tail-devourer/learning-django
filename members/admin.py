from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "joined_date")
    prepopulated_fields = { "slug": ("first_name", "last_name") }


admin.site.register(Member, MemberAdmin)
