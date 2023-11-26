from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages

from .models import ContactInfo, Request
from .forms import RequestForm


def contact(request):
    contact_info = ContactInfo.objects.first()
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your request has been received successfully, we will contact you soon')
            return redirect(reverse_lazy('contact'))

    context = {
        'contact_info': contact_info,
        'form': form
    }
    return render(request, 'contact/index.html', context)
