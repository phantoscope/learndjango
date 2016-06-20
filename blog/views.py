#coding:utf-8
from django.shortcuts import render_to_response
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_index(request):
    #获取文章列表
    article = Article.objects.all().order_by('-date_publish')

    #文章列表分页
    paginator = Paginator(article, 4)
    page = request.GET.get('page')
    try:
        article_list = paginator.page(page)
    except PageNotAnInteger:
        article_list = paginator.page(1)
    except EmptyPage:
        article_list = paginator.page(paginator.num_pages)

    return render_to_response('blog/blog-index.html', {'article_list':article_list})
