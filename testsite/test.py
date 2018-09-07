# test.py
from random_choose import choose
import random
if __name__ == '__main__':
    url_pro = choose()
    probability = []
    url = []
    for i in range(len(url_pro)):
        tmp = []
        probability.append(url_pro[i][0])
        for j in range(1, len(url_pro[i])):
            tmp.append(url_pro[i][j])
        url.append(tmp)
    print probability
    print url

