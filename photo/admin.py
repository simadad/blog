from django.contrib import admin
from photo.models import Album, Photo


class PhotoInline(admin.TabularInline):
    model = Photo

admin.site.register(Album)
admin.site.register(Photo)
