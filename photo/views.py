from django.shortcuts import render, get_object_or_404
from models import Album, Photo
# from myblog.models import Blogger
from django import forms
from PIL import Image
from django.http import HttpResponse
from django.core.files.uploadedfile import InMemoryUploadedFile
import StringIO
# Create your views here.


class ImgForm(forms.Form):
    photo = forms.ImageField()


def index(request):
    albums = Album.objects.all().order_by('-Revise_date')[:6]
    info = {}
    for eve_album in albums:
        photos = eve_album.Photos.all().order_by('id')[:6]
        info[eve_album] = {
            'album': eve_album,
            'photos': photos,
            'page': 1
        }
    return render(request, 'photo/index.html', {
        'albums': info,
    })


def album(request):
    album_id = request.GET.get('id')
    album_box = get_object_or_404(Album, id=album_id)
    if request.method == 'POST':
        photo_files = request.FILES.getlist('photo')
        for photo_file in photo_files:
            photo_name = photo_file.name
            thumbnail_ph = get_thumbnail(photo_file, photo_name)
            new_photo = Photo.objects.create(
                Orig_photo=photo_file,
                Thumbnail_photo=thumbnail_ph
            )
            album_box.Photos.add(new_photo)
    photos = album_box.Photos.all().order_by('id')[:6]
    return render(request, 'photo/album.html', {
        'photos': photos,
        'album': album_box
    })


def get_thumbnail(img, name):
    image = Image.open(img)
    image.thumbnail((150, 150), Image.ANTIALIAS)
    thumb_io = StringIO.StringIO()
    image.save(thumb_io, format='JPEG')
    image_file = InMemoryUploadedFile(thumb_io, None, name, 'image/jpeg', thumb_io.len, None)
    return image_file

'''
def ajax_index(request):
    albums = Album.objects.all().order_by('-Revise_date')[:5]
    info = {}
    for eve_album in albums:
        photos = eve_album.Photos.all().order_by('id')[:5]
        info[eve_album] = photos
    return HttpResponse(render(request, 'photo/ajax_index.html', info))
'''


def ajax_index_photos(request):
    page = int(request.GET.get('page'))
    album_id = int(request.GET.get('album_id'))
    page_add = request.GET.get('add')
    print page, album_id, page_add
    ajax_album = get_object_or_404(Album, id=album_id)
    if page_add == 'true':
        page += 1
    else:
        page -= 1
    photos = ajax_album.Photos.all().order_by('id')[page*6-6: page*6]
    if photos:
        info = {
            'page': page,
            'photos': photos,
            'album': ajax_album
        }
        return HttpResponse(render(request, 'photo/ajax_index_photos.html', {
            'album': info
        }))
    else:
        return HttpResponse()


def ajax_index_big(request):
    photo_id = request.GET.get('photo_id')
    big_photo = get_object_or_404(Photo, id=photo_id)
    return HttpResponse(render(request, 'photo/ajax_index_big.html', {
        'photo': big_photo
    }))


def ajax_album_photos(request):
    page = int(request.GET.get('page'))
    album_id = int(request.GET.get('album_id'))
    album_box = get_object_or_404(Album, id=album_id)
    photos = album_box.Photos.all().order_by('id')[page * 6 - 6: page * 6]
    return HttpResponse(render(request, 'photo/ajax_album_photos.html', {
        'photos': photos
    }))
