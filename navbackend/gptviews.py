from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def user_login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = authenticate(request, email=email, password=password)
    
    if user is not None:
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def user_signup(request):
    email = request.data.get('email')
    password = request.data.get('password')
    fname = request.data.get('fname')
    lname = request.data.get('lname')

    user = User.objects.create_user(email=email, password=password)
    user.first_name = fname
    user.last_name = lname
    user.save()

    return Response({'message': 'Signup successful'}, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def user_logout(request):
    logout(request)
    return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)

# {
#   "email": "john.doe@example.com",
#   "fname": "John",
#   "lname": "Doe",
#   "password": "123456"
# }
