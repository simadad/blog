# coding: utf-8
from __future__ import unicode_literals
from myblog.models import Blogger
from django.db import models
# Create your models here.


class Album(models.Model):
    Name = models.CharField('相册名', max_length=20, default='ALBUM')
    Owner = models.ForeignKey(Blogger, on_delete=models.CASCADE, related_name='Albums')
    Create_date = models.DateTimeField('建册时间', auto_now_add=True)
    Revise_date = models.DateTimeField('最后修改', auto_now=True)
    # Cover = models.ForeignKey(Photo, on_delete=models.SET_DEFAULT, default=)

    def __str__(self):
        return self.Name


class Photo(models.Model):
    Name = models.CharField('照片名', max_length=20, default='PHOTO')
    Orig_photo = models.ImageField(upload_to='img/photo', default='../static/photo/image/default.jpg')
    Thumbnail_photo = models.ImageField(upload_to='img/photo/thumbnail', blank=True)
    Album = models.ManyToManyField(Album, 'Photos')

    def __str__(self):
        return self.Name
