from . tokens import generate_token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from . mailexpress import mailexpress
from .models import candiate
# from django.utils.encoding import force_bytes,force_text
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
    obj = candiate(email=email, firstname=fname, lastname=lname)  # Create a new instance and assign values

    obj.save() 
    
    myuser=User.objects.create_user(username=email,email=email,password=password)
    myuser.first_name=fname
    myuser.last_name=lname
    myuser.is_active=True
    myuser.save()
    current_site=get_current_site(request)
    name=myuser.first_name
    domain=current_site.domain
    # uid=urlsafe_base64_encode(force_bytes(myuser.pk))
    token=generate_token.make_token(myuser)
    email_subject="Confirm Your email to use navigator"
    email_body=f"""
                    <html>

<body >

   <div style=" align-items: center; justify-content: center; width: 100%; flex-direction: row;">
    <p style="font-size: 17px; width: 100%;color:#000;">
        Hello {name}! <br>Welcome to Navigator. Please <b>Verify</b> your email to create your account.
        <br>To verify your account, click on the button below.
    </p>
    <br><br>
    <div style="width: 100%;">
        <a href="http://{domain}/verify/{token}">
            <button style="height: 50px; width: 150px; background-color: #3770CC; color: rgb(255, 251, 251); border: none; font-size: 20px; cursor: pointer;">
                Verify Account
            </button>
        </a>
    </div>
</div>


</html>

                """
    
    empty=[]
    
    mailexpress(email,email_subject,email_body,empty)

    return Response({'message':'Signup sucessful'},status=status.HTTP_201_CREATED)
    


@api_view(['GET'])
def signout(request):
    logout(request)
    return Response({'message':'Log out sucessfully'},status=status.HTTP_200_OK)


# def activate(request,uidb64,token):
#     try:
#         uid=force_text(urlsafe_base64_decode(uidb64))
#         myuser=User.objects.get(pk=uid)
#     except(TypeError,ValueError,OverflowError,User.DoesNotExist):
#         myuser=None
#     if myuser is not None and generate_token.check_token(myuser,token):
#         myuser.is_active=True
#         myuser.save()
#         login(request,myuser)
#     else:
#         pass