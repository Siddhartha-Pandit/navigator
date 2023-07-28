from django.urls import path
from . import views
urlpatterns=[
    path('signin/',views.signin,name='signin'),
    path('signup/',views.signup,name='signout'),
    path('signout/',views.signout,name='signout'),
    path('allcandidate/',views.allcandidate,name='allcandidate'),
    path('personalinfoget/<str:email>',views.personalinfoget,name='getpersonalinfo'),
    path('personalinfopost/<str:email>',views.personalinfopost,name='postpersonalinfo'),
    path('hrassign/<str:hrstaff>',views.assignedcandiate,name='assignhr'),
    path('selection/<str:candidate>',views.selected,name='selection'),
    
    path('verify/<uidb64>/<token>',views.activate,name='activate'),
    
]
# url = f"http://{domain}{reverse('activate')}?uidb64={uid}&token={token}"
# http://{{domain}}{% url 'activate' uidb64=uid token=token %}