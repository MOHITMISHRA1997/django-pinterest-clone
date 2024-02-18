from django.contrib import admin
from .models import MyBaseUser,Profile,Follow


# Register your models here.


admin.site.register(MyBaseUser)
admin.site.register(Profile)
admin.site.register(Follow)
