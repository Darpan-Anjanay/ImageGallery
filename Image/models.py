from django.db import models
from django.contrib.auth.models import User
import uuid
import os




class Profile(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    ProfileImgName  =  models.ImageField( upload_to = 'Profile')

class Album(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    AlbumName = models.CharField(max_length=255,null=False,blank=False)
    def __str__(self):
        return self.AlbumName


class Image(models.Model):
    User = models.ForeignKey(User,on_delete=models.CASCADE)
    Image = models.ImageField( upload_to = 'Images')
    Album = models.ForeignKey(Album,on_delete=models.CASCADE)
    Created_at = models.DateTimeField(auto_now_add=True)
    Modified_at = models.DateTimeField(null=True,blank=True)
    SoftDelete = models.BooleanField(default=False)
    Trash = models.BooleanField(default=False)


    @property
    def size_mb(self):
        return self.Image.size / (1024 * 1024)
    