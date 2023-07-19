from django.shortcuts import get_object_or_404
from . tokens import generate_token
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from . mailexpress import mailexpress
from django.template.loader import render_to_string
from .models import User
# from django.utils.encoding import force_bytes, force_text
from django.utils.encoding import force_bytes,force_str
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
   
    
    myuser=User.objects.create_user(email=email,password=password)
    myuser.first_name=fname
    myuser.last_name=lname
    myuser.is_email_verified=False
    myuser.is_active=False
    myuser.save()
    current_site=get_current_site(request)
    message2=render_to_string('confirmemial.html',{
        'name':myuser.first_name,
        'domain':current_site.domain,
        'uid':urlsafe_base64_encode(force_bytes(myuser.pk)),
        'token':generate_token.make_token(myuser)
    })
    email_subject="Confirm Your email to use navigator"
#     email_body=f"""
                 

#                 """
    #  url = f"http://{domain}{reverse('activte')}?uidb64={uid}&token={token}"
    # http://{{domain}}{% url 'activte' uidb64=uid token=token %}
    
    empty=[]
    
    mailexpress(email,email_subject,message2,empty)

    return Response({'message':'Signup sucessful'},status=status.HTTP_201_CREATED)
    


@api_view(['GET'])
def signout(request):
    logout(request)
    return Response({'message':'Log out sucessfully'},status=status.HTTP_200_OK)



@api_view(['GET'])
def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = get_object_or_404(User,pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
       return Response({'message':'Invalid activation link'},status=404)
    if generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.is_email_verified=True
        myuser.save()
        login(request, myuser)
        return Response({'message':'Verified sucessfully'},status=200)
    else:
        return Response({'message':'activation failed please try again'},status=400)
    # Rest of the code...
