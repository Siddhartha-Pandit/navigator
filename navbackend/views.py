from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
@api_view(['POST'])
def signin(request):
 
    email=request.data.get('email')
    password=request.data.get('password')
    user=authenticate(request,username=email,password=password)
    if user is not None:
        login(request,user)
        return Response({'message':'login_sucessfully'},status=status.HTTP_200_OK)
    else:
        return Response({'message':'Invalid cresidenetail'},status=status.HTTP_401_UNAUTHORIZED)
   

@api_view(['POST'])
def signup(request):
   
    email=request.data.get('email')
    password=request.data.get('password')
    fname=request.data.get('fname')
    lname=request.data.get('lname')
  
    
    myuser=User.objects.create_user(username=email,email=email,password=password)
    myuser.first_name=fname
    myuser.last_name=lname
    myuser.save()

    return Response({'message':'Signup sucessful'},status=status.HTTP_201_CREATED)
    


@api_view(['GET'])
def signout(request):
    logout(request)
    return Response({'message':'Log out sucessfully'},status=status.HTTP_200_OK)

