# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from imageUpload.models import Img
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import os
from random_choose import choose
from django.contrib import messages
from ShowResults.models import Result_Img

# Create your views here.
@csrf_exempt
def analyze(request):
    request.session.set_expiry(0)
    #fo = open("form.txt", "a")
    if request.method == "POST":
        check_box_list = request.POST.getlist("check_box_list")
        list0 = request.session.get('list0')
        if not list0:
            queryset = []
            for i in range(len(list0)):
                img0 = Img.objects.get(img_name__exact=list0[i])
                queryset.append(img0)
            messages.error(request, "Please upload an image.")
            return render(request, 'list.html', {'queryset': queryset, 'check_box_list': check_box_list})

        if check_box_list:
        # for i in range(len(list0)):
        # fo.write(str(list0[i]))
            list = ','.join(check_box_list)
            print list
            #fo.write("OK")

            url_pro = choose(list0[0])

            Result_images = []

            for i in range(len(url_pro)):
                img = Result_Img()
                r = []
                for j in range(2, len(url_pro[i])):
                    r.append(url_pro[i][j])
                img.Result_probability = url_pro[i][0]
                img.Result_name = url_pro[i][1]
                img.Result_path= r
                Result_images.append(img)
            queryset = []
            for i in range(len(list0)):
                img0 = Img.objects.get(img_name__exact=list0[i])
                queryset.append(img0)
            return render(request, 'conclusion.html',  {'Result_images': Result_images, 'queryset': queryset, 'list':list})
        else:
            # for i in range(len(list0)):
            # fo.write(str(list0[i]))
            #fo.write("NO")
            messages.warning(request, "Please choose a measure.")
            queryset = []
            for i in range(len(list0)):
                img0 = Img.objects.get(img_name__exact=list0[i])
                queryset.append(img0)
            return render(request, 'list.html', {'queryset': queryset, 'check_box_list': check_box_list})
    else:
        check_box_list = []
        list0 = request.session.get('list0')
        queryset = []
        for i in range(len(list0)):
            img0 = Img.objects.get(img_name__exact=list0[i])
            queryset.append(img0)
        return render_to_response('list.html', {'queryset': queryset, 'check_box_list': check_box_list})

@csrf_exempt
def continue_img(request):
    request.session.set_expiry(0)
    list0 = request.session.get('list0')
    #fo = open("form.txt", "a")
    #fo.write("3")
    return HttpResponseRedirect('/image')

@csrf_exempt
def delete_image(request, id):
    request.session.set_expiry(0)
    id = int(id)
    list0 = request.session.get('list0')
    img0 = Img.objects.get(img_name__exact=list0[id])
    os.remove(settings.MEDIA_ROOT + '/' + str(img0.img))
    Img.objects.get(img_name__exact=list0[id]).delete()
    list0.remove(list0[id])
    request.session['list0'] = list0
    return HttpResponseRedirect('/result')


@csrf_exempt
def refresh(request):
    request.session.set_expiry(0)
    list0 = request.session.get('list0')
    for i in range(len(list0)):
        img0 = Img.objects.get(img_name__exact = list0[i])
        os.remove(settings.MEDIA_ROOT + '/' + str(img0.img))
        Img.objects.get(img_name__exact = list0[i]).delete()
    queryset = []
    request.session['list0'] = []
    check_box_list = []
    return render_to_response('list.html', {'queryset': queryset, 'check_box_list': check_box_list})


@csrf_exempt
def logout(request):
    list0 = request.session.get('list0')
    for i in range(len(list0)):
        img0 = Img.objects.get(img_name__exact = list0[i])
        os.remove(settings.MEDIA_ROOT + '/' + str(img0.img))
        Img.objects.get(img_name__exact = list0[i]).delete()
    del request.session['account']  #删除session
    del request.session['list0']
    return HttpResponseRedirect('/login')
