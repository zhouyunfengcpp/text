# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv('test.csv')
dict = df[['title']].to_dict()['title']
f = open('jianyan.txt','w',encoding='utf-8')
for key in dict:
    f.write(dict[key]+'\n')
f.close