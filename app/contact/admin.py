from django.contrib import admin

from .models import ContactInfo, Request

admin.site.register(ContactInfo)
admin.site.register(Request)
