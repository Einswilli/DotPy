from django.shortcuts import render,redirect
from django import template
from django.core.checks import messages
from django.db.models.expressions import Value
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.core.mail import send_mail
# Create your views here.
def home(request):
    return render(request,'index.html')


def sendMail(request):
    if request.method=='POST':
        print(request.POST['name'])
        print(request.POST['email'])
        print(request.POST['subject'])
        print(request.POST['message'])

        content=f"""
        Nom     : {request.POST['name']}
        EMAIL   : {request.POST['email']}

        Message : {request.POST['message']}
        """

        send_mail(
            request.POST['subject'],
            content,
            request.POST['email'],
            ['wilfriedgoeh@gmail.com']
        )
        send_mail(
            "Notification de service!",
            "un nouveau projet vient d'arriver!",
            "#DotPy notifyer",
            ['wilfriedgoeh@gmail.com','augustev005@gmail.com','novenosexta77@gmail.com']
        )
        #print('envoyé!')

        return HttpResponse(status=204)

