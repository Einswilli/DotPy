from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="Home"),
    path("sendMail",views.sendMail,name="sendMail"),
    path("connexion",views.connexion,name="connexion"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("table",views.table,name="table"),
    path("icons",views.icons,name="icons"),
    path("reset-pass",views.passreset,name="reset-pass"),
    path("register",views.register,name="register")
    ]