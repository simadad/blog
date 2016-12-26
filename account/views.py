# coding: utf-8
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from myblog.models import Blogger
from django.http import HttpResponse
from weibo import APIClient

# Create your views here.




def get_client():
    APP_KEY = 219696178
    APP_SECRET = '46967d372ca931c9b8596567fe9784e5'
    CALLBACK_URL = 'http://simadad0520.pythonanywhere.com/account/login'
    client = APIClient(APP_KEY, APP_SECRET, CALLBACK_URL)
    return client


def weibo(request):
    client = get_client()
    url = client.get_authorize_url()
    return redirect(url)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create_user(
            username=username,
            password=password,
        )
        Blogger.objects.create(
            User=user,
            id=user.id,
            Nickname=username
        )
        login(request, user)
        return HttpResponse(render(request, 'account/logout.html'))
    else:
        pass
    return render(request, 'account/register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            user = User.objects.get(username=username)
            if user.blogger.Status:
                login(request, user)
                return HttpResponse(render(request, 'account/logout.html'))
            else:
                return HttpResponse(render(request, 'account/missing_blogger.html'))
        else:
            return HttpResponse(render(request, 'account/not_match.html'))
    else:
        client = get_client()
        code = request.GET.get('code')
        r = client.request_access_token(code)
        access_token = r.access_token
        expires = r.expires
        uid = int(r.uid)
        client.set_access_token(access_token, expires)
        info = client.users.show.get(uid=uid)
        nickname = info['name']
        username = 'wb'+info['idstr']
        exist_users = User.objects.filter(username=username)
        if exist_users:
            weibo_user = exist_users[0]
        else:
            weibo_user = User.objects.create_user(username=username)
            Blogger.objects.create(
                User=weibo_user,
                id=weibo_user.id,
                Nickname=nickname
                )
        login(request, weibo_user)
        # a = client.users.show.get()
        # print client.statuses.user_timeline.get(), 11111111111
        # print client.statuses.update.post(status=u'测试OAuth 2.0发微博'), 222222222222
        return render(request, 'myblog/index.html')


def log_out(request):
    logout(request)
    return HttpResponse(render(request, 'account/login.html'))
