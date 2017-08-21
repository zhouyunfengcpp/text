# -*- coding: utf-8 -*-
import pandas as pd


df = pd.read_csv('result.csv')
adas = df[df['classify']==df['检验']]
print('正确数为：'+str(adas.__len__()))
df = df[df['classify']!=df['检验']]
a = df.groupby('classify').count()
dict_a = a.to_dict()
# print()
dd = pd.read_csv('test.csv')
b = dd.groupby('classify').count()
dict_b = b.to_dict()
# print(b)
for key in dict_a['title']:
    percentage = int(dict_a['title'][key])/int(dict_b['title'][key])
    print(str(key)+'当中错误占比为'+str(percentage))
    