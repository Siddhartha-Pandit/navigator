import random
from django.shortcuts import get_object_or_404
from . tokens import generate_token
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.permissions import IsAuthenticated
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from . mailexpress import mailexpress
from django.template.loader import render_to_string
from .models import User,Candidate,hrstaff,isselected
# from django.utils.encoding import force_bytes, force_text
from django.utils.encoding import force_bytes,force_str
from .serializers import UserSerializers,CandidateSerializer,SelectedSerializer
# from .permission import CanUpdateorReadonly
@api_view(['POST'])
def signin(request):
 
    email=request.data.get('email')
    password=request.data.get('password')
    user=authenticate(request,username=email,password=password)
    if user is not None:
        if user.is_email_verified:
        
            login(request,user)
            serializer = UserSerializers(user)
           
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response({'message':'Email not verified'},status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message':'Invalid cresidenetail'},status=status.HTTP_401_UNAUTHORIZED)
                        
   
   

@api_view(['POST'])
def signup(request):
   
    email=request.data.get('email')
    password=request.data.get('password')
    fname=request.data.get('fname')
    lname=request.data.get('lname')
    hr_staff = hrstaff.objects.all()
   
    
    myuser=User.objects.create_user(email=email,password=password)
    user=Candidate.objects.create_user(email=email,password=password)
    selected = isselected.objects.create(candidate=user)
    myuser.first_name=fname
    myuser.last_name=lname
    myuser.user_type="candidate"
    user.is_email_verified=True
    myuser.is_active=False
    assigned_hr = random.choice(hr_staff)
    user.assigned_hr = assigned_hr
    selected.email=email
    selected.save()
    user.save()
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


@api_view(['GET'])
def personalinfoget(request, email):
    try:
        # candidate = get_object_or_404(Candidate, email=email)
        candidate = Candidate.objects.get(email=email)
        print(candidate)
    except Candidate.DoesNotExist:
        return Response({'message': 'Candidate not found'}, status=status.HTTP_404_NOT_FOUND)

 
    serializer = CandidateSerializer(candidate)  # Use the CandidateSerializer to serialize Candidate model data
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def assignedcandiate(request, hrstaff):
    try:
        # candidate = get_object_or_404(Candidate, email=email)
        candidate = Candidate.objects.filter(assigned_hr=hrstaff)
       
    except Candidate.DoesNotExist:
        return Response({'message': 'Candidate not found'}, status=status.HTTP_404_NOT_FOUND)

 
    serializer = CandidateSerializer(candidate,many=True)  # Use the CandidateSerializer to serialize Candidate model data
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def allcandidate(request):
    try:
        # candidate = get_object_or_404(Candidate, email=email)
        candidate = Candidate.objects.all()
        print(candidate)
    except Candidate.DoesNotExist:
        return Response({'message': 'Candidate not found'}, status=status.HTTP_404_NOT_FOUND)

 
    serializer = CandidateSerializer(candidate,many=True)  # Use the CandidateSerializer to serialize Candidate model data
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def selected(request,candidate):
    try:
        selected = isselected.objects.get(candidate=candidate)
    except isselected.DoesNotExist:
        return Response({'message': 'Selected candidate not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = SelectedSerializer(instance=selected, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
@api_view(['PUT'])
def personalinfopost(request, email):
    try:
        # Fetch the candidate based on the provided email, which is the primary key (email field).
        candidate = Candidate.objects.get(email=email)
    except Candidate.DoesNotExist:
        return Response({'message': 'Candidate not found'}, status=status.HTTP_404_NOT_FOUND)

    # Now, we can update the candidate object with the data from the request.
    serializer = CandidateSerializer(instance=candidate, data=request.data,partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# from rest_framework.permissions import BasePermission

# class IsCandidate(BasePermission):
#     def has_permission(self, request, view):
#         return request.user.user_type == 'candidate'

# from .permissions import IsCandidate

# @api_view(['POST'])
# @permission_classes([IsAuthenticated, IsCandidate])
# def personalinfo(request):
#     # Your existing code here
#     # ...


        
