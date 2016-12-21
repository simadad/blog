from django.conf.urls import url, include
from . import views

ajax_url = [
    url(r'^IndexPhotos', views.ajax_index_photos, name='index_photos'),
    url(r'^IndexBigPhoto', views.ajax_index_big, name='index_big'),
    url(r'AlbumPhotos', views.ajax_album_photos, name='album_photos'),
]


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^album', views.album, name='album'),
    url(r'^ajax/', include(ajax_url, namespace='ajax')),
]
