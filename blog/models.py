# coding: utf-8
from django.db import models
import datetime
from django.utils import timezone


class MailTag(models.Model):
    mail_name = models.CharField(max_length=255) 
    mail_tags = models.CharField(max_length=255)
    mail_mails = models.IntegerField(max_length=255)    

    
    
class Mail(models.Model):
    mail_name = models.CharField(max_length=255) 
    datetime = models.DateTimeField(u'Дата',auto_now_add=True) 
    mail_numb = models.IntegerField(max_length=255)
    mail_mails = models.IntegerField(max_length=255)
    
    def __unicode__(self):
        return self.mail_name

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
        
class Tags(models.Model):
    tags_name = models.CharField(max_length=255) 
    
class Komment(models.Model):
    id_post = models.IntegerField(max_length=255) 
    datetime = models.DateTimeField(auto_now_add=True) 
    content = models.TextField(max_length=1000) 
    name = models.TextField(max_length=100)
    def __unicode__(self):
        return self.content

    def get_absolute_url(self):
        return "/blog/%i/" % self.id

    title = models.CharField(max_length=255) 
    publivation_date = models.DateTimeField(u'Дата публикации',auto_now_add=True) 
    publisher = models.TextField(max_length=10000)
    authors = models.CharField(max_length=255) 

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
