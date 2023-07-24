from rest_framework.permissions import BasePermission

class CanUpdateorReadonly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ['GET','HEAD','OPTIONS']:
            return request.user.user_type=='hr'
        
        return False
    def has_object_permission(self, request, view, obj):
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.user_type == 'hr'
        elif request.method == 'POST':
            return request.user.user_type == 'candidate' and request.user == obj.user
        
        return False
    
#     {
# "email":"connect2ranjitsingh@gmail.com",
# "user_type":"candidate",
# "password":"abc",
# "dob":"2023-07-24",
# "gender":"MALE",
# "mobile":"122334"
# }