#coding:utf-8
from django.http import HttpResponse


def blog_index(request):
    return HttpResponse(u"Hello Django")
