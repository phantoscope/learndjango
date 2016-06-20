#coding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.blog_index,name='blog_index'),
    url(r'^article/(\d+)',views.blog_article,name='blog_article'),
]
