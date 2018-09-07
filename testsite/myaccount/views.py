# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from myaccount.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

#定义表单模型
class Register_form(forms.Form):
    username = forms.CharField(label='username',max_length=100)
    email = forms.EmailField(label='email')
    password = forms.CharField(label='password',widget=forms.PasswordInput())
    password_confirm = forms.CharField(label='password_confirm',widget=forms.PasswordInput())

class Login_form(forms.Form):
    account = forms.CharField(label='account',max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput())

@csrf_exempt

# Create your views here.
def signup(request):
    request.session.set_expiry(0)
    if request.method == "POST":
        uf = Register_form(request.POST)
        if uf.is_valid():
            #获取表单信息

            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            password_confirm = uf.cleaned_data['password_confirm']
            email = uf.cleaned_data['email']
            user_name = User.objects.filter(username__exact=username)
            user_email = User.objects.filter(email__exact=email)

            if user_name:
                messages.error(request, "the username is exist.")
                return render(request, 'new_index2.html', {'uf': uf})

            if user_email:
                messages.error(request, "the email is exist.")
                return render(request, 'new_index2.html', {'uf': uf})

            if (password==password_confirm):
                #将表单写入数据库
                user = User()
                user.username = username
                user.password = password
                user.email = email
                user.save()
                #返回注册成功页面
                messages.success(request, "you have successfully created an account.")
                return render(request, 'new_index1.html',{'uf': uf})
            else:
                uf = Register_form()
                messages.error(request, "the two password are different.")
                return render(request, 'new_index2.html', {'uf': uf})
        else:
            messages.warning(request, "information is not complete.")
            return render(request, 'new_index2.html', {'uf': uf})


    else:
        uf = Register_form()
        return render_to_response('new_index2.html',{'uf':uf})
@csrf_exempt
def login(request):
    request.session.set_expiry(0)
    if request.method == "POST":
        uf = Login_form(request.POST)
        if uf.is_valid():

            #获取表单信息
            account = uf.cleaned_data['account']
            password = uf.cleaned_data['password']
            # 获取的表单数据与数据库进行比较
            name_exit = User.objects.filter(username__exact=account)
            email_exit = User.objects.filter(username__exact=account)
            if not (name_exit or email_exit):
                messages.error(request, "The account is not exist.")
                return render(request, 'new_index1.html', {'uf': uf})


            user_name = User.objects.filter(username__exact=account, password__exact=password)
            user_email = User.objects.filter(email__exact=account, password__exact=password)
            if user_name or user_email:
                if not ('account' in request.session):
                    list0 = []
                    request.session['account'] = account
                    request.session['list0'] = list0
                else:
                    if (request.session['account']!=account):
                        list0 = []
                        request.session['account'] = account
                        request.session['list0'] = list0
                        request.session['form'] = ImgForm()
                return HttpResponseRedirect('/image')
            else:
                messages.error(request, "your account or password is not correct.")
                return render(request, 'new_index1.html', {'uf': uf})
        else:
            messages.warning(request, "information is not complete.")
            return render(request, 'new_index1.html', {'uf': uf})
    else:
        uf = Login_form()
        return render(request, 'new_index1.html',{'uf':uf})



