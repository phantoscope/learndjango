#coding:utf-8
from django.shortcuts import render_to_response
from models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#文章列表
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


    return render_to_response('blog/blog_index.html', {'article_list':article_list})


# 文章详情
def blog_article(request,blog_id):
    article = Article.objects.get(id=blog_id)

    #更新浏览数
    article.view_count += 1
    article.save()

    return  render_to_response('blog/blog_article.html', {'article':article,'request':request})