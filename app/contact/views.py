from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib import messages

from .forms import RequestForm
from .models import ContactInfo


def contact(request):
    contact_info = ContactInfo.objects.first()
    form = RequestForm()
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Success')
            return redirect(reverse_lazy('contact'))

    context = {
        'contact_info': contact_info,
        'form': form
    }
    return render(request, 'contact/index.html', context)
