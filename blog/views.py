from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category, Banner


# Create your views here.
def hello(request):
    return HttpResponse('hello!')


#首页
def index(request):
    allcategory = Category.objects.all()
    banner = Banner.objects.filter(is_active=True)[0:4]
    context = {'allcategory': allcategory,
               'banner': banner}
    return render(request, 'index.html', context)


#列表页
def list(request,lid):
    return render(request, 'list.html')


#内容页
def show(request,sid):
    return render(request, 'show.html')


#标签页
def tag(request, tag):
    pass


# 搜索页
def search(request):
    pass


# 关于我们
def about(request):
    pass