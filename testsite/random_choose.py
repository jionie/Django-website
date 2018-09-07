# -*- coding: utf-8 -*-
import os
import cv2
import numpy
from pylab import *
import math
from match import *
import random

def choose(query_image_name):
    ################################################################################



    pos = query_image_name.rfind('#')
    exact_dir = query_image_name[:pos].replace(' ', '')


    cwd = os.getcwd()
    dir_path = cwd + "/picture source/"
    static_path = "/picture source/"

    type = os.listdir(dir_path)
    index = []
    probability = []
    print exact_dir
    print type.index(exact_dir)
    for i in range(len(type)):
        tmp = 0.8*math.exp((random.uniform(1, 5)-3)**2/(-2))
        index.append(i)
        probability.append(tmp)


    for j in range(len(index)-1):
        for k in range(j+1, len(index)):
            if probability[j] < probability[k]:
                tmp = probability[j]
                probability[j] = probability[k]
                probability[k] = tmp
                tmp_index = index[j]
                index[j] = index[k]
                index[k] = tmp_index

    if probability[0]<0.5:
        while probability[0] > 0.3:
            probability.append(probability[0])
            del probability[0]
            index.append(index[0])
            del index[0]
        while probability[0] <= 0.3:
            del probability[0]
            del index[0]

    else:
        while probability[0] > 0.5:
            probability.append(probability[0])
            del probability[0]
            index.append(index[0])
            del index[0]
        while probability[0] <= 0.5:
            del probability[0]
            del index[0]

    exist = -1
    for p in range(len(index)):
        if type[index[p]] == exact_dir:
            exist = p
            break

    if exist == -1:
        tmp = probability[0]
        probability.insert(0, min(tmp+0.05, 1.0))
        index.insert(0, type.index(exact_dir))

    else:
        tmp = probability[0]
        del probability[exist]
        del index[exist]
        probability.insert(0, min(tmp + 0.05, 1.0))
        index.insert(0, type.index(exact_dir))

    print probability
    print index



    queryset = []
    for p in range(len(index)):
        type_name = type[index[p]]
        type_path = dir_path + type_name + "/"
        pics = []
        pics.append(probability[p])
        pics.append(type_name)
        imgs = os.listdir(type_path)
        for i in range(len(imgs)):
            img_name = imgs[i]
            num = random.randint(0,99)
            if num < 50:
                pics.append(static_path + type_name + "/" + img_name)
            else:
                if (i == (len(imgs) - 4)) and (len(pics)==2):
                    pics.append(static_path + type_name + "/" + img_name)
                elif (i == (len(imgs) - 3)) and (len(pics)==3):
                    pics.append(static_path + type_name + "/" + img_name)
                elif (i == (len(imgs) - 2)) and (len(pics)==4):
                    pics.append(static_path + type_name + "/" + img_name)
                elif (i == (len(imgs) - 1)) and (len(pics)==5):
                    pics.append(static_path + type_name + "/" + img_name)

            if len(pics) == 6:
                break
        print pics
        queryset.append(pics)

    return queryset




if __name__ == '__main__':
    choose()
