# -*- coding: utf-8 -*-
import codecs 
import pandas as pd
import numpy as np


keys = ['港股','国内财经','基金','美股','期货','生活','外汇','证券']
stop = ['~','！','@','#','￥','%','…','………','&','*','（','）','《','》','：','(',')',':']
dict = {}
for each in keys:
    path = 'temp\\'+str(each)+'\\topic_word.txt'
    f = codecs.open(path,'r',encoding='utf-8')
    a = f.readlines()
    list = []
    for each_a in a:
        each_a = each_a[8:].replace('\n','')
        for each_stop in stop:
            if each_stop in each_a:
                aaa = each_a.find(each_stop)
                each_a = each_a.replace(str(each_stop)+' ','')
#         print(each_a)
        while(' ' in each_a):
            aaa = each_a.find(' ')
            temp = each_a[:aaa]
            each_a = each_a[aaa+1:]
            list.append(temp)
#             print(each_a)
#     print(list)
    dict[each]=list

f = codecs.open('jianyan.txt','r',encoding='utf-8')
score = {'港股':[],'国内财经':[],'基金':[],'美股':[],'期货':[],'生活':[],'外汇':[],'证券':[]}
list_str = []
a = f.readlines()
for each_a in a:
    for key in dict:
        count = 0
        for each_cont in dict[key]:
            if each_cont in each_a:
                count = count + 1
#         if(key=='证券'):
#             count = count*3/4
        score[key].append(count)
    list_str.append(each_a)


title = pd.Series(list_str)
score_ganggu = pd.Series(score['港股'])
score_guonei = pd.Series(score['国内财经'])
score_jijin = pd.Series(score['基金'])
score_meigu = pd.Series(score['美股'])
score_qihuo = pd.Series(score['期货'])
score_shenghuo = pd.Series(score['生活'])
score_waihui = pd.Series(score['外汇'])
score_zhengquan = pd.Series(score['证券'])
dd = pd.read_csv('test.csv')['classify']
ttt = {'title':title,'港股':score_ganggu,'国内财经':score_guonei,'基金':score_jijin,'美股':score_meigu,'期货':score_qihuo,'生活':score_shenghuo,'外汇':score_waihui,'证券':score_zhengquan,'classify':dd}
df = pd.DataFrame(ttt,columns=['title','港股','国内财经','基金','美股','期货','生活','外汇','证券','classify'])
df.to_csv('jianyan.csv',encoding='utf-8')