#coding:utf-8
from django.contrib import admin
from blog.models import *
from django.conf import settings

class ArticleAdmin(admin.ModelAdmin):

    list_display = ('title', 'desc', 'view_count','is_recommend','date_publish')
    list_display_links = ('title', 'desc', )
    list_editable = ('view_count',)

    class Media:
        js = (
                settings.STATIC_URL + 'kindeditor/kindeditor-all-min.js' ,
                settings.STATIC_URL + 'kindeditor/plugins/code/prettify.js',
                settings.STATIC_URL + 'kindeditor/lang/zh_CN.js',
                settings.STATIC_URL + 'kindeditor/config.js',
        )

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)
