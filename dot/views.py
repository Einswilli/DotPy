from django.shortcuts import render,redirect
from django import template
from django.core.checks import messages
from django.db.models.expressions import Value
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.core.mail import send_mail
from .models import *
# Create your views here.
def home(request):
    return render(request,'index.html')

def connexion(request):
    return render(request,'login.html')

def dconnexion(request):
    return render(request,'dlogin.html')

def dlogin(request):
    
    un=request.POST.get('username')
    up=request.POST.get('pass')
    #c=request.POST.get('design')
    msg=''
    #try:
    try:
        au=Designer.objects.get(DesignerEmail=un,DesignerPass__exact=up)
        msg=None
        return render(request,'ddash.html',{'msg':msg,'user':au})
    except:
        msg="utilisateur ou mot de passe incorrect !"
        return render(request,'dlogin.html',{'msg':msg})
    # except:
    #     msg="utilisateur ou mot de passe incorrect !"
    #     return render(request,'dlogin.html',{'msg':msg})

def login(request):
    un=request.POST.get('username')
    up=request.POST.get('pass')
    #c=request.POST.get('design')
    msg=''

    try:
        
        u=User.objects.get(UserEmail=un,UserPass__exact=up)
        if u is not None:
            msg=None
            return render(request,'dashboard.html',{'msg':msg})
        else:
            msg="utilisateur ou mot de passe incorrect !"
            return render(request,'login.html',{'msg':msg})
    except:
        msg="utilisateur ou mot de passe incorrect !"
        return render(request,'login.html',{'msg':msg})

def dashboard(request):
    return render(request,'dashboard.html')

def table(request):
    return render(request,'tables.html')

def icons(request):
    return render(request,'icons.html')

def passreset(request):
    return render(request,'reset-password.html')

def register(request):
    return render(request,'register.html')

def store(request):
    # for i in range(Designer.objects.all().count()):
    #     Designer.objects.filter(DesignerID=i).delete()
    #     print('deleted!')
    return render(request,'store.html')

def dsign(request):
    return render(request,'dregister.html')

def dregister(request):
    try:
        try:
            ds=Designer.objects.get(DesignerFName=request.POST.get('fname'),DesignerLName=request.POST.get('lname'),DesignerEmail=request.POST.get('email'),DesignerNumber=request.POST.get('number'),)
        
            return render(request,'dregister.html',{'msg':"Un compte existe déjà avec les même information"})
        except:
            #return render(request,'dregister.html',{'msg':"Un compte existe déjà avec les même information"})

            d=Designer.objects.create(
                    DesignerFName=request.POST.get('fname'),
                    DesignerLName=request.POST.get('lname'),
                    DesignerEmail=request.POST.get('email'),
                    DesignerNumber=request.POST.get('number'),
                    DesignerJob=request.POST.get('jtitle'),
                    DesignerPass=request.POST.get('pass'),
                    DesignerPhoto=request.FILES.get('Photo')
                )
            if d:
                print("enregistré!")
                return render(request,'ddash.html',{'user':Designer.objects.get(DesignerFName=request.POST.get('fname'),DesignerLName=request.POST.get('lname'),DesignerPass=request.POST.get('pass'),)})
            return render(request,'dregister.html',{'msg':"Formulaire invalide"})
    except:
        return render(request,'dregister.html',{'msg':"Formulaire invalide"})

        
def signup(request):
    
    u=User.objects.create(
        UserFName=request.POST.get('fname'),
        UserLName=request.POST.get('lname'),
        UserEmail=request.POST.get('email'),
        UserNumber=request.POST.get('number'),
        UserJob=request.POST.get('jtitle'),
        UserPass=request.POST.get('pass'),
        UserPhoto=request.FILES.get('Photo')
    )
    if u:
        return render(request,'dashboard.html')
    return render(request,'register.html',{'msg':"Formulaire invalide"})

def sendMail(request):
    if request.method=='POST':
        # print(request.POST['name'])
        # print(request.POST['email'])
        # print(request.POST['subject'])
        # print(request.POST['message'])

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

