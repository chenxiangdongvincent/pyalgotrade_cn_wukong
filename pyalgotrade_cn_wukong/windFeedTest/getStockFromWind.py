# -*- coding: utf-8 -*-
"""
Created on Tue May 23 09:22:15 2017

@author: Think
"""

import pandas as pd
from WindPy import *
from WindPy import w
import datetime, time
import os

class WindStock():
    def getCurrentTime(self):
        return time.strftime('[%Y-%m-%d %H:%M:%S]', time.localtime(time.time()))
    
    def AStockHisData(self,symbols,start_date,end_date,step=0):
        
        count = 0
        print (self.getCurrentTime(),":Download stock starting ")
        for symbol in symbols:     #遍历股票池
           
            #download bein 
            if count == 10:         #下载前十只股票
                return
            print "handle one symbol"
      
            try:
                
                #前复权方式
                stock = w.wsd(symbol, "open,high,low,close,volume,amt",start_date,end_date, "adjDate=0;unit=1;PriceAdj=F")
   
                index_data = pd.DataFrame()
                index_data['Date'] = stock.Times
                index_data['Open'] = stock.Data[0]
                index_data['High'] = stock.Data[1]
                index_data['Low'] = stock.Data[2]
                index_data['Close'] = stock.Data[3]
                index_data['Volume'] = stock.Data[4]
                index_data['Adj Close'] = stock.Data[3]      #需要修改
                
                index_data.to_csv("dataFile/"+str(symbol)+ ".csv",index = False)  #去除索引
                
            except Exception as e:
                print "Exceptin : %s" %(e)
                    
            count +=1
        
            
        print (self.getCurrentTime(),":download stock has finished")
        return
    
    def getAStockCodesFromCsv(self):
        #file_path = os.path.join(os.getcwd(),'Stock.csv')
        return 
    
    def getAStockCodesWind(self,end_date):
     
        stockCodes=w.wset("sectorconstituent","date="+end_date+";sectorid=a001010100000000;field=wind_code")
        if stockCodes.ErrorCode!=0:
            print "get data failed, exit!"
            return None
        else:
            return stockCodes.Data[0]  #  ??

def main():
    
    
    w.start()
    
    windstock = WindStock()
    start_date = '20170520'
    end_date = '20170529'
    
    #获取A股所有的股票代码
    symbols=windstock.getAStockCodesWind(end_date)   
    
    fm = pd.DataFrame(symbols)
    fm = fm.T
    print fm
    windstock.AStockHisData(symbols, start_date,end_date)
    
    #save the data into csv files

    w.stop()
        
if __name__ == "__main__":
    main()

        
        
        
        
        
        
        
        
        
        
        
            
        