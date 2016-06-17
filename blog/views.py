#coding:utf-8
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

'''
def blog_index(request):
    return HttpResponse(u"Hello Django")
'''


def blog_index(request):
    now = datetime.datetime.now()
    otherStyleTime = now.strftime("%Y-%m-%d %H:%M:%S")
    text = "Welcom to learn django"
    return render_to_response('blog/index.html',locals())
