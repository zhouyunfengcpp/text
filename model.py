# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn import cross_validation


df = pd.read_csv('jianyan.csv')[['港股','国内财经','基金','美股','期货','生活','外汇','证券','classify']]
data = []
label = []
for i in range(df.__len__()):
    dict = df.iloc[i:i+1].to_dict()
    temp = []
    temp.append(dict['港股'][i])
    temp.append(dict['国内财经'][i])
    temp.append(dict['基金'][i])
    temp.append(dict['美股'][i])
    temp.append(dict['期货'][i])
    temp.append(dict['生活'][i])
    temp.append(dict['外汇'][i])
    temp.append(dict['证券'][i])
    data.append(temp)
    label.append(dict['classify'][i])

x = data
y = label
x_train,x_test,y_train,y_test=cross_validation.train_test_split(x,y,test_size=0.2)
x_train = x[:1300]
x_test = x[1300:]
y_train = y[:1300]
y_test = y[1300:]
clf=tree.DecisionTreeClassifier(criterion='gini')
clf.fit(x_train,y_train)
anwser1=clf.predict(x_train)
print(anwser1)
anwser2=clf.predict(x_test)
print(anwser2)
anwser = np.concatenate((anwser1,anwser2))
ass = pd.Series(anwser)
ddd = pd.read_csv('jianyan.csv')
ddd['检验'] = ass
ddd.to_csv('result.csv',encoding='utf-8')
ddd.to_csv('result_see.csv')