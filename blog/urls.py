#coding:utf-8
from django.conf.urls import url
from . import views
from learndjango.upload import upload_image


urlpatterns = [
    url(r'^$',views.blog_index,name='blog_index'),
    url(r'^article/(\d+)',views.blog_article,name='blog_article'),
    url(r'^add/$', views.blog_add, name='blog_add'),
    #前端kindeditor编辑器上传图片处理函数
    url(r'^upload/(?P<dir_name>[^/]+)$',upload_image,name='blog_uploadimg'),
]