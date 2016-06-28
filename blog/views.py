#coding:utf-8

from django.shortcuts import render_to_response,redirect,get_object_or_404
from django.template.loader import render_to_string
from django.template import RequestContext
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


#前端增加文章
def blog_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        category = request.POST['category']
        tag = request.POST.getlist('tag')
        #涉及到POST传递过来的数据包含普通数据和多对多,一对多数据,先处理完(保存)标准数据,在处理特殊数据
        #对于外键的数据处理
        foreignkey_cacategory = Category.objects.get(id=category) #先在分类表中查询出choice选中分类对应对象
        b = Article(title=title,content=content,category=foreignkey_cacategory)
        b.save()
        #处理多对多数据
        for blog_tag in tag:
            b.tag.add(blog_tag)
        b.save()

        #保存完post传递过来的所有数据,然后需要重定向页面,在django1.9,直接写入要重定向相应view函数名即可
        return redirect('blog_article',b.id)

    #处理get请求
    category = Category.objects.all()
    tag = Tag.objects.all()

    #下面这种方法示从1.10之后提,这种写法已经停用
    return render_to_response(
        'blog/blog_add.html',
        {'category':category,'tag':tag},
        context_instance=RequestContext(request)
    )
