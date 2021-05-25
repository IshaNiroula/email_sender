from django.shortcuts import render
from myproject.settings import EMAIL_HOST_USER

from django.core.mail import send_mail

from . import forms

# Create your views here.


def subscribe(request):
    sub = forms.Subscribe()
    if request.method == 'POST':
        sub = forms.Subscribe(request.POST)
        subject = "Welcome to Isha's Mail Server"
        message = "Hope you are enjoying this :D :D"
        receipent = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER,
                  [receipent], fail_silently=False)

        context = {"receipent": receipent}

        return render(request, 'subscribe/success.html', context)

    context = {
        'form': sub
    }
    return render(request, 'subscribe/index.html', context)
