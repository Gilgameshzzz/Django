from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse

from essay.forms import UserForm
from essay.models import Users, UserTicket
# Create your views here.
from utils.functions import get_ticket


def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')


def register(request):
    if request.method == 'GET':
        # 如果请求为get,返回注册页面
        return render(request, 'register.html')

    if request.method == 'POST':
        # 校验参数
        form = UserForm(request.POST)
        # 判断is_valid()是否为True
        if form.is_valid():
            # 注册,使用make_password 进行密码加密，否则为明文
            password = make_password(form.cleaned_data['password'])
            Users.objects.create(
                username=form.cleaned_data['username'],
                password=password
            )
            # 跳转到登录界面,使用namespace：name
            return HttpResponseRedirect(reverse('essay:login'))
        else:
            return render(request, 'register.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = Users.objects.filter(username=form.cleaned_data['username']).first()
            if user:
                if check_password(form.cleaned_data['password'], user.password):
                    res = HttpResponseRedirect(reverse('essay:index'))
                    ticket = get_ticket()
                    res.set_cookie('ticket', ticket, max_age=1000)
                    UserTicket.objects.create(user=user, ticket=ticket)
                    return res
                else:
                    return render(request, 'login.html')
            else:
                return render(request, 'login.html')
        else:
            return render(request, 'login.html')


def article(request):
    if request.method == 'GET':
        return render(request, 'article.html')


def comment(request):
    if request.method == 'GET':
        return render(request, 'comment.html')


def category(request):
    if request.method == 'GET':
        return render(request, 'category.html')


def manage_user(request):
    if request.method == 'GET':
        return render(request, 'manage-user.html')


def flink(request):
    if request.method == 'GET':
        return render(request, 'flink.html')


def notice(request):
    if request.method == 'GET':
        return render(request, 'notice.html')


def setting(request):
    if request.method == 'GET':
        return render(request, 'setting.html')


def readset(request):
    if request.method == 'GET':
        return render(request, 'readset.html')


def add_article(request):
    if request.method == 'GET':
        return render(request, 'add-article.html')


def add_category(request):
    if request.method == 'GET':
        return render(request, 'add-category.html')


def add_flink(request):
    if request.method == 'GET':
        return render(request, 'add-flink.html')


def add_notice(request):
    if request.method == 'GET':
        return render(request, 'add-notice.html')


def update_article(request):
    if request.method == 'GET':
        return render(request, 'update-article.html')


def update_category(request):
    if request.method == 'GET':
        return render(request, 'update-category.html')


def update_flink(request):
    if request.method == 'GET':
        return render(request, 'update-flink.html')


def loginlog(request):
    if request.method == 'GET':
        return render(request, 'loginlog.html')


