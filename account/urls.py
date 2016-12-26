from django.conf.urls import url
from account import views

urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^login', views.log_in, name='login'),
    url(r'^logout', views.log_out, name='logout'),
    url(r'^weibo', views.weibo, name='weibo'),
]
