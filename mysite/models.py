# coding: utf-8
from django.db import models
import datetime
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=255) 
    datetime = models.DateTimeField(u'Дата публикации') 
    content = models.TextField(max_length=10000) 

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return "/blog/%i/" % self.id
    
class Komment(models.Model):
    id_post = models.IntegerField(max_length=255) 
    datetime = models.DateTimeField(auto_now_add=True) 
    content = models.TextField(max_length=10000) 
    
    def __unicode__(self):
        return self.content

    def get_absolute_url(self):
        return "/blog/%i/" % self.id


    

class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.question

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Опубликовано?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text




