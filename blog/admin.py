# coding: utf-8
from django.contrib import admin
from blog.models import Mail,Komment




class MailAdmin(admin.ModelAdmin):
    list_display = ('mail_name', 'datetime')
    search_fields = ('mail_name',)
    list_filter = ('datetime',)
    date_hierarchy = 'datetime'
    ordering = ('-datetime',)

class KommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'content', 'datetime')
    search_fields = ('name',)
    list_filter = ('datetime',)
    date_hierarchy = 'datetime'
    ordering = ('-datetime',)


admin.site.register(Mail,MailAdmin)
admin.site.register(Komment,KommentAdmin)
