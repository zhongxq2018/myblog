from django.shortcuts import render
from django.http import HttpResponse
from .models import Article


# Create your views here.
def hello(request):
    return HttpResponse('hello!')


def home(request):
    return render(request, 'home.html')


def index(request):
    sitename = 'Django中文网'
    url = 'www.django.cn'

    allarticle = Article.objects.all()

    list = [
        '开发前的准备',
        '项目需求分析',
        '数据库设计分析',
        '创建项目',
        '基础配置',
        '欢迎页面',
        '创建数据库模型',
    ]
    mydict={
        'name': '吴秀峰',
        'qq': '445813',
        'wx': 'vipdjango',
        'email': '445813@qq.com',
        'Q群': '10218442',
    }
    context = {
        'sitename': sitename,
        'url': url,
        'list': list,
        'mydict': mydict,
        'allarticle': allarticle,
    }

    return render(request, 'index.html', context)
