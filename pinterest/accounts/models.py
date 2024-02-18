from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .manager import MyUserManager

# Create your models here.

class MyBaseUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length = 50,unique = True)
    username = models.CharField(max_length = 50,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin    



#Createing User profile
    
class Profile(models.Model):
    user = models.OneToOneField(MyBaseUser,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profiles",default="profiles/default.png")
    about = models.TextField()
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    pronouns = models.CharField(max_length=50)
    website = models.CharField(max_length=50)

    def __str__(self):
        return str(self.user)
    



class Follow(models.Model):
    follower = models.ForeignKey(MyBaseUser,on_delete = models.CASCADE,related_name="followers")
    following = models.ForeignKey(MyBaseUser,on_delete = models.CASCADE,related_name="following")

    def __str__(self) -> str:
        return f'{self.follower} is following {self.following}'
    



    

