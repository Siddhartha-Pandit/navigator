from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse("This is login page")

def signup(request):
    return HttpResponse("This is Sign up page")

def logout(request):
    return HttpResponse("This is log out page")

