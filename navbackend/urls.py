from django.urls import path
from . import views
urlpatterns=[
    path('',views.signin,name='signin'),
    path('signup',views.signup,name='signout'),
    path('signout',views.signout,name='signout'),
    
]