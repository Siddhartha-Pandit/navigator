from rest_framework.permissions import BasePermission

class CanUpdateorReadonly(BasePermission):
    def has_permission(self, request, view):
        # Allow HR users to read candidate details
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.user_type == 'hr'
        # Deny all other methods for HR users
        elif request.user.user_type == 'hr':
            return False
        # Candidates can only read and update their own details
        return True

    def has_object_permission(self, request, view, obj):
        # HR users can view candidate details but not update
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return request.user.user_type == 'hr'
        
        # Candidates can update their own details
        if request.user.user_type == 'candidate' and request.user == obj.user:
            return True

        # HR can update email and is_email_verified fields in User model
        if request.user.user_type == 'hr':
            allowed_fields = ['email', 'is_email_verified']
            return all(
                getattr(obj, field) == getattr(request.data, field) for field in allowed_fields
            )
        
        # HR can update the Selected model
        if request.user.user_type == 'hr' and view.basename == 'selected':
            return True

        # Deny all other write permissions
        return False
