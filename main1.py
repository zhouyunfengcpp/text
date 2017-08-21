# -*- coding: utf-8 -*-
import tushare as ts

import numpy as np
import pandas as pd

import text.cleaning as cleaning
import text.LDAtest as LDAtest

# ts.set_token('c38545a128fb1c59cf36579fff22b911d1ddb8b6138b24f69ae85361e5b5c763')
# fd = ts.Subject('SocialDataXQ')
# a = ts.get_latest_news(top=100, show_content=True)
# a = ts.get_latest_news(top=100)[['calssify','title','time']]
df = ts.get_latest_news(top=50000)[['classify','title']]
df.to_csv('test.csv',encoding='utf-8')
# a.to_csv('test.csv',encoding='utf-8')
print('main1 OKOKOK')

keys = cleaning.precleaning()
for key in keys:
    LDAtest.ldaaa(key)