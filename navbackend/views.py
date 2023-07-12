from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
    user=authenticate(request,email=email,password=password)
    if user is not None:
        login(request,user)

    return HttpResponse("This is login page")

def signup(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
    
    myuser=User.objects.create_user(request,email,password)
    myuser.first_name=fname
    myuser.last_name=lname
    myuser.save()

    return HttpResponse("This is Sign up page")

def logout(request):
    return HttpResponse("This is log out page")

