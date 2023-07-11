from django.urls import path
from . import views
urlpatterns=[
    path('',views.login,name='login'),
    path('signup',views.signup,name='signout'),
    path('logout',views.logout,name='logout'),
    
]