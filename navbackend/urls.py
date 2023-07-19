from django.urls import path
from . import views
urlpatterns=[
    path('',views.signin,name='signin'),
    path('signup/',views.signup,name='signout'),
    path('signout/',views.signout,name='signout'),
    path('verify/<uidb64>/<token>',views.activate,name='activate'),
    
]
# url = f"http://{domain}{reverse('activate')}?uidb64={uid}&token={token}"
# http://{{domain}}{% url 'activate' uidb64=uid token=token %}