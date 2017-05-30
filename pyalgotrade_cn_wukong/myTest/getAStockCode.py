# -*- coding: utf-8 -*-
"""
Created on Mon May 22 13:14:34 2017

@author: Think
"""

from WindPy import *
import json
from WindPy import w
import pandas as pd

w.start()


#获取所有A股代码#
AllAStock =w.wset("SectorConstituent","date=20151122;sectorId=a001010100000000;field=wind_code");
if AllAStock.ErrorCode != 0:
    print("Get Data failed! exit!")
    exit()
    
fm = pd.DataFrame(AllAStock.Data)
fm = fm.T
print fm

fm.to_csv('AllStock.csv')

#with open('AllAStock.json',mode='w') as f2:json.dump(AllAStock.Data[0],f2);

w.stop()