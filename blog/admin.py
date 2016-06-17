#coding:utf-8
from django.contrib import admin
from blog.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'view_count','is_recommend','date_publish')
    list_display_links = ('title', 'desc', )
    list_editable = ('view_count',)



# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Article,ArticleAdmin)
