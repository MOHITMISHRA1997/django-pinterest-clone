from django.db import models
from accounts.models import MyBaseUser


# Create your models here.

class Board(models.Model):
    user = models.ForeignKey(MyBaseUser,on_delete=models.CASCADE,related_name = "board_user")
    title = models.CharField(max_length=100)
    pins = models.ManyToManyField('pins.Pin',related_name="pins",blank=True)
    cover = models.ImageField(upload_to="boards",default="boards/default.png")
    is_private = models.BooleanField(default = False)
    description = models.TextField()

    def __str__(self):
        return self.title

    
