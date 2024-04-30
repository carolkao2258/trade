# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 00:12:30 2024

@author: User
"""

import yfinance as yf
stocks=['2314','2321','2332','2345','2419','3047','3062','3138','3596','5388']
for i in stocks:
    df=yf.download(i+".TW","2020-01-01","2023-12-31")
    df.to_csv('yahoo_'+i+'TW.csv')
    
import pandas as pd
url1 ="https://raw.githubusercontent.com/johnny147852/fin_data/main/"
list1=["2701","2702","2704","2705","2706","2707","2712","2722","2723","2727"]
for i in list1:
    url = url1+"yahoo_"+i + "TW.csv"
    df1 = pd.read_csv(url, index_col=0)#index_col表示從第一個欄位開始找
    df.to_csv("yahoo_"+i+'TW.csv')

import pandas as pd
url2 ="https://raw.githubusercontent.com/jenny172/fin_data/main/"
list2=["2323","2409","3059","3149","3481","3504","3714","4934","6164","6176"]
for j in list2:
    ur2 = url2+"yahoo_"+j + "TW.csv"
    df = pd.read_csv(ur2, index_col=0)#index_col表示從第一個欄位開始找
    df.to_csv("yahoo_"+j+'TW.csv')
    


