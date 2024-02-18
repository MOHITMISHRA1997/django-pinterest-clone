from django.db import models
from accounts.models import MyBaseUser
from boards.models import Board
from mimetypes import guess_type

# Create your models here.

class Pin(models.Model):
    user = models.ForeignKey(MyBaseUser,on_delete=models.CASCADE,related_name = "pin_user")
    title = models.CharField(max_length = 50)
    board = models.ForeignKey(Board,on_delete = models.CASCADE,related_name = "boards")
    posted_on = models.DateTimeField(auto_now_add = True)
    file = models.FileField(upload_to="pins")
    link = models.CharField(max_length = 50)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title
    

    def get_type(self):
        file_type = guess_type(self.file.url, strict= True)[0]
        if 'video' in file_type:
            return 'video'
        elif 'image' in file_type:
            return 'image'


