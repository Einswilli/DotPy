from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="Home"),
    path("sendMail",views.sendMail,name="sendMail"),
    path("connexion",views.connexion,name="connexion"),
    path("dconnexion",views.dconnexion,name="dconnexion"),
    path("dashboard",views.dashboard,name="dashboard"),
    path("table",views.table,name="table"),
    path("icons",views.icons,name="icons"),
    path("reset-pass",views.passreset,name="reset-pass"),
    path("register",views.register,name="register"),
    path("dregister",views.dregister,name="dregister"),
    path("dsign",views.dsign,name="dsign"),
    path("login",views.login,name="login"),
    path("dlogin",views.dlogin,name="dlogin"),
    path("signup",views.signup,name="signup"),
    path("store",views.store,name="store"),
    ]