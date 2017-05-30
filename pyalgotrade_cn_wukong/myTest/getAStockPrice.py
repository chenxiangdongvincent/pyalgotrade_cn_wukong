# -*- coding: utf-8 -*-
"""
Created on Mon May 22 09:41:03 2017

@author: Think

"""

from WindPy import w
from datetime import *
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from datetime import datetime

#启动WindPy插件
w.start()

if w.isconnected() == True:
    print "wind api connected successfully"
else:
    print "wind api connected failed"
    

def printpy(outdata):
    if outdata.ErrorCode!=0:
        print('error code is'+str(outdata.ErrorCode)+'\n')
        return
    for i in range(0,len(outdata.Data[0])):    #行数
        strTemp = ''
        if len(outdata.Times)>1:
            strTemp = str(outdata.Times[i]) +' '
        for k in range(0, len(outdata.Fields)):
            strTemp = strTemp + str(outdata.Data[k][i]) + ' '
        print strTemp
                  

#提取价格数据    
#wsd序列   获取status等其他非数字列时有格式问题
#wsddata1 = w.wsd("000001.SZ", "open,high,low,close,volume,amt","2017-4-22","2017-5-21","Fill=Previous")
#wsddata1 = w.wsd("000001.SZ", "open,high,low,close,volume,amt",datetime.today()-timedelta(10))
wsddata1 = w.wsd("000001.SZ", "open,high,low,close,volume,amt","2016-5-1",datetime.today()-timedelta(1))
#printpy(wsddata1)


fm = pd.DataFrame(wsddata1.Data, index =wsddata1.Fields, columns=wsddata1.Times )
print fm.T
fm = fm.T
fm.to_csv("000001.csv")








w.stop()
