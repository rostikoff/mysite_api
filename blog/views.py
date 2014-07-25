# coding: utf-8
from blog.models import Mail, Komment, Tags , MailTag
import datetime
from django.utils import timezone
from django.shortcuts import get_object_or_404,render_to_response, redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.template import RequestContext
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import urllib
from xml.dom.minidom import parse
import xml.dom.minidom
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from math import *
from django.db.models import Max

from blog.forms import ContactForm,LoginForm



#global переменные
#  path = api_url + api_metod + ".xml?token=" + api_token + api_param
api_token = 'd7ac05a85997048a3e6ea16f657c58923475f1d48df43bc2fbfcd482'
api_url = 'https://pddimp.yandex.ru/'
mail_page = 5.0 #формат ввода 2.0(два ТОЧКА ноль)
domain_name = '@testapi.ssido.ru'



def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Правильный пароль и пользователь "активен"
        auth.login(request, user)
        # Перенаправление на "правильную" страницу
        return HttpResponseRedirect("/")
    else:
        # Отображение страницы с ошибкой
        return render_to_response('blog/api_logerr.html', {'error': 'true'})

def logout(request):
    auth.logout(request)
    # Перенаправление на страницу.
    return HttpResponseRedirect("/")
    
def login_views(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                if form.get_user():
                    login(request, form.get_user())
                    return HttpResponseRedirect('/')
        else:
            form = LoginForm()
        return render_to_response('blog/api_login.html', {'form': form},context_instance=RequestContext(request))
    else:
        #данные о ящиках в базу данных                 &on_page='+str(mail_page)+'
        data = xml_res_par(request,'get_domain_users','&page=1','email','name', '2')
        #количество страниц обработка
        data_count = Mail.objects.all().count()
        max_page = data_count / mail_page
        max_page=int(ceil(max_page))
        #категории для фильтра
        all_filtr = Tags.objects.all()
        #данные из бд
        data = Mail.objects.all()
        data = data.order_by('-mail_numb')
        paginator = Paginator(data, int(mail_page))
        page1 = paginator.page(1)   

        return render_to_response('blog/api_index.html', {"data": page1.object_list, "page": '1', "domain_name": domain_name, 'max_page': max_page, 'all_filtr': all_filtr,'mail_page':int(mail_page),'data_count':data_count,},context_instance=RequestContext(request))
    
    
def xml_res_par(request, api_metod, api_param, sch1, sch2, param):
#на входе имя метода, параметры(формат &on_page=100&page=1 ), что ищем(строку email-sch1 а в ней name-sch2) - на выходе данные 
    #data = urllib.urlopen(path).read()
    path = api_url + api_metod + ".xml?token=" + api_token + api_param
    DOMTree = xml.dom.minidom.parse(urllib.urlopen(path))
    collection = DOMTree.documentElement
    movies = collection.getElementsByTagName(sch1)
    data = []
    data5 = dict()
    data6 = dict() 
    if param == '2':
        Mail.objects.all().delete()
        max = Mail.objects.all().aggregate(Max('mail_numb'))
        i = max['mail_numb__max']
        for movie in movies:
            type = movie.getElementsByTagName(sch2)[0]
            mail_unread = xml_res_seachattr(request,'get_mail_info','&login='+type.childNodes[0].data,'new_messages')
            str = type.childNodes[0].data
            str = str.split('@')
            try:
                i=i-1
            except TypeError :
                i = 1000
            #data5[str[0]] = mail_unread['res']
            data5 = {'email' : str[0], 'mess' : mail_unread['res']}
            data6 [ i ] = data5
            qwe = str[0]
            sch = Mail.objects.filter(mail_name__exact=qwe)
            if len(sch) == 0:                
                m = Mail(
                    mail_name = qwe,
                    mail_mails = mail_unread['res'],
                    mail_numb = i,
                )
                m.save()
                sch = MailTag.objects.filter(mail_name__exact=qwe)
                if len(sch) == 0:
                    m2 = MailTag(
                        mail_name = qwe,
                        mail_mails = 0,                        
                        mail_tags = 1,
                    )
                    m2.save()
                
        data1 = data6
        sync_mail_mailtag(request)
    else:
        for movie in movies:
            type = movie.getElementsByTagName(sch2)[0]
            data.append(type.childNodes[0].data)
        data1 = {sch1: data, } 
        
    
    
    return data1

def xml_res_str(request, api_metod, api_param, sch1):
#на проверка на наличие тега в xml документе
    path = api_url + api_metod + ".xml?token=" + api_token + api_param
    data = []
    data5 = urllib.urlopen(path).read()
    res = data5.find(sch1)
    if res == -1:
        data.append('-')
    else:
        data.append('+')
    data1 = {'res': data, } 
    
    return data1 

def xml_res_seachattr(request, api_metod, api_param, sch1):
#проверка на наличие атрибута в xml документе
    path = api_url + api_metod + ".xml?token=" + api_token + api_param
    data = []
    data5 = urllib.urlopen(path).read()
    res = data5.find(sch1)
    if res == -1:
        data.append('-')
    else:
        res1 = data5[(res+len(sch1)+2):]
        res2 = res1.find('"')
        res3 = res1[:res2]
        
        
        
    data1 = {'res': res3, } 
    
    return data1     
  
def reg_user_token(request):
    if request.is_ajax():
        name=request.POST.get("name", "")
        passw1=request.POST.get("pass1", "")
        passw2=request.POST.get("pass2", "")
        if passw1==passw2:
            passw = passw1        
            data = xml_res_str(request,'reg_user_token','&u_login='+name+'&u_password='+passw,'ok')
            li = data['res']
            if  "+" in li:
                message = "Пользователь успешно добавлен"
                type_err = 0
                lcount = Mail.objects.all().count()
                nuu = Mail.objects.all().aggregate(Max('mail_numb'))
                m = Mail(
                    mail_name = name,
                    mail_tags = 1,
                    mail_mails = 0,
                    mail_numb = nuu['mail_numb__max']+1,
                )
                m.save()
            else:
                type_err = 1
                if len(passw)<1 or len(name)<1:
                    message = "Введите корректные данные"
                else:
                    if name == passw:
                        message = "Логин и пароль не могут быть одинаковыми"
                    else:
                        if len(passw)<6:
                            message = "Пароль слишком короткий"
                        else:
                            message = "Такой пользователь уже существует"
        else:
            type_err = 1
            message = "Пароли не совпадают"   
    else:
        type_err = 1
        message = "Ошибка сервера, обратитесь к админу"
    data = [type_err,message]
    return HttpResponse(data)
    
@csrf_exempt
def xml_res_pagin(request):
    if request.is_ajax():
        page=int(request.POST.get("page", ""))
        sost=request.POST.get("sost", "")
        filtr=request.POST.get("filtr", "")
        
        #количество страниц обработка
        if filtr=='1':
            data_count = Mail.objects.all().count()
            data = Mail.objects.all()
        else:
            data_count = MailTag.objects.filter(mail_tags__exact=filtr).count()
            data = MailTag.objects.filter(mail_tags__exact=filtr)
            #data = Mail.objects.filter(mail_name__exact=data1)
        
        max_page = data_count / mail_page
        max_page=int(ceil(max_page))
        
        #data = data.order_by('-mail_numb')
        paginator = Paginator(data, int(mail_page))
        
        if sost=='r':
            page = page +1                
        if sost=='l':
            page = page - 1
        page1 = paginator.page(page)    

    return render_to_response('blog/api_paginate.html', {"data": page1.object_list,"page": page,"domain_name": domain_name , 'max_page': max_page,'mail_page':int(mail_page),'data_count':data_count, })  

@csrf_exempt
def delete_user(request):
    if request.is_ajax():
        data=str(request.POST.get("data", ""))
        data = data.split(',')
        for name in data:
            name = str(name) 
            if name != '':
                data1 = xml_res_str(request,'delete_user','&login='+str(name),'ok') 
                qwe = str(name)
                Mail.objects.filter(mail_name__exact=qwe).delete()
                message = "Удалено"                    
            else:       
                message = "Неверное имя"   
    return HttpResponse(message)      
 

def sync_mail_mailtag(request):
    data = Mail.objects.all()
    for data in data:
        sch = MailTag.objects.get(mail_name=data.mail_name)
        sch.mail_mails = data.mail_mails
        sch.save()
    data2 = MailTag.objects.all()
    #for data2 in data2:
        #sch2 = Mail.objects.get(mail_name=data2.mail_name)
        #if (sch.mail_mails==''):
        #    MailTag.objects.get(mail_name=data2.mail_name).delete()
    res = 1
    return res  
    
