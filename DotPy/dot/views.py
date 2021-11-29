from django.shortcuts import render,redirect
from django import template
from django.core.checks import messages
from django.db.models.expressions import Value
from django.http.response import HttpResponse
# Create your views here.
def home(request):
    return render(request,'index.html')
