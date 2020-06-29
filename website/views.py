from django.core.mail import send_mail
from django.shortcuts import render

from website.models import Setting, FAQ


def home(request):
    return render(request, 'home.html', {})


def aboutus(request):
    return render(request, 'about.html', {})


def contact(request):
    if request.method == "POST":
        message_name = request.POST['message-name']
        message_email = request.POST['message-email']
        message = request.POST['message']

        send_mail(
            message_name,
            message,
            message_email,
            [''],
        )

        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})


def pricing(request):
    return render(request, 'pricing.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def faq(request):
    return render(request, 'faq.html', {})
