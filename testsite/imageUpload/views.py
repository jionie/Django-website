# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.files.base import ContentFile
from imageUpload.models import Img
from django import forms
from django.shortcuts import render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.conf import settings
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import cv2
import os


class ImgForm(forms.Form):
    img = forms.FileField()


@csrf_exempt
def upload(request):
    request.session.set_expiry(0)
    list0 = request.session.get('list0')
    if request.method == "POST":
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            iimg = form.cleaned_data['img']
            i = Img()
            tmp_name = str(iimg)
            i.img = iimg
            i.img_id = len(list0)
            while (tmp_name in list0):
                tmp_name = tmp_name + "_"

            i.img_name = tmp_name
            i.save()
            list0.append(tmp_name)
                #fo = open("form.txt", "a")
            #for i in range(len(list0)):
                #fo.write(str(list0[i]))
                #fo.write(str(iimg))
            request.session['list0'] = list0
            """"
            img_path = settings.MEDIA_ROOT+'/'+ list0[0]
            img = cv2.imread(img_path)
            cv2.imshow("img",img)
            k = cv2.waitKey(0)
            if k == 27:  # wait for ESC key to exit
                cv2.destroyAllWindows()
            elif k == ord('s'):  # wait for 's' key to save and exit
                cv2.imwrite('copy_test.png', img)
                cv2.destroyAllWindows()
            """
            queryset = []
            for i in range(len(list0)):
                img0 = Img.objects.get(img_name__exact=list0[i])
                queryset.append(img0)
            return render_to_response('new_index.html', {'form': form, 'queryset':queryset})
        else:
            messages.error(request, "invalid image.")
            form = ImgForm()
            queryset = []
            for i in range(len(list0)):
                img0 = Img.objects.get(img_name__exact=list0[i])
                queryset.append(img0)
            return render_to_response('new_index.html', {'form': form, 'queryset': queryset})
    else:
        form = ImgForm()
        queryset = []
        if list0:
            for i in range(len(list0)):
                img0 = Img.objects.get(img_name__exact=list0[i])
                queryset.append(img0)
    return render_to_response('new_index.html', {'form': form, 'queryset':queryset})

@csrf_exempt
def delete_Image(request, id):
    request.session.set_expiry(0)
    id = int(id)
    list0 = request.session.get('list0')
    img0 = Img.objects.get(img_name__exact=list0[id])
    os.remove(settings.MEDIA_ROOT + '/' + str(img0.img))
    Img.objects.get(img_name__exact=list0[id]).delete()
    list0.remove(list0[id])
    request.session['list0'] = list0
    return HttpResponseRedirect('/image')




@csrf_exempt
def clear(request):
    request.session.set_expiry(0)
    list0 = request.session.get('list0')
    for i in range(len(list0)):
        img0 = Img.objects.get(img_name__exact = list0[i])
        os.remove(settings.MEDIA_ROOT + '/' + str(img0.img))
        Img.objects.get(img_name__exact = list0[i]).delete()
    messages.success(request, "the query images are refreshed.")
    request.session['list0'] = []
    return HttpResponseRedirect('/image')

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
