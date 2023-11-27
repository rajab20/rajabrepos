from django.shortcuts import render
from contact.models import ContactInfo

def index(request):
    return render(request, 'home/index.html')
