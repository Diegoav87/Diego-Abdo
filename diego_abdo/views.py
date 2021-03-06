from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']

        template = render_to_string('email_template.html', {
            'name': request.POST['name'],
            'email': request.POST['email'],
            'message': request.POST['message']
        })

        email = EmailMessage(
            "Sitio Web",
            template,
            settings.EMAIL_HOST_USER,
            ['diegoabdov@gmail.com']
        )
        email.fail_silently = False
        email.send()
        return render(request, 'contact_confirm.html', {"name": name})
    else:
        return render(request, 'index.html')
