# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

import jieba

def precleaning():
    df = pd.read_csv('test.csv')[['classify','title']]
    df_temp = df.groupby('classify').count()
    aa = df_temp.to_dict()['title']
    keys = []
    for key in aa:
        keys.append(key)
        temp = df[df['classify']==key].reindex()['title']
        dict = temp.to_dict()
        f = open('temp\\'+str(key)+'.txt','w')
        for key in dict:
            f.write(str(dict[key])+'\n')
        f.close
    return keys
    print('precleaning OKOKOK')
    
# def 