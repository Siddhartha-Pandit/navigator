from django.contrib import admin
from .models import candidate,hrstaff,employee,User
# from .models import User

admin.site.register(User)
admin.site.register(candidate)
admin.site.register(hrstaff)
admin.site.register(employee)

# Register your models here.
