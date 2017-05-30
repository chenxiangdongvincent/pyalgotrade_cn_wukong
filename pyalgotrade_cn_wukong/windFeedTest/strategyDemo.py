# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:41:50 2017

@author: Think
"""

from pyalgotrade import strategy
from pyalgotrade.barfeed import windfeed
from pyalgotrade.broker.backtesting import TradePercentage

from pyalgotrade.stratanalyzer import returns
from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.stratanalyzer import trades

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed,instruments):
        strategy.BacktestingStrategy.__init__(self,feed,10000)  #初始化资金为10000元
        #self.getBroker().setCommission(TradePercentage(0.001)) #设置佣金比例
        self.setUseAdjustedValues(False)
        self.__instruments = instruments  #获取标的股票代码
        self.__position = None
   
   
    def onEnterOk(self, position):
        execInfo = position.getEntryOrder().getExecutionInfo()
        print "\n deal at price" + str(execInfo.getPrice()) + "\n"
        
    def onExitOk(self, position):
        #execInfo = position.getExitOrder().getExecutionInfo()
        #print "\n sell at price" + str(execInfo.getPrice()) + "\n"
        pass
        
    
    def onBars(self,bars):
        
        
        totalEquity = self.getBroker().getEquity()
        positions = self.getBroker().getPositions()
        cash = self.getBroker().getCash()

      
        print "datetime is " + str(bars.getDateTime())
        print "total equity is " + str(totalEquity)
        print "total cash is " + str(cash)
        print "total positions is " + str(positions)
        
        
        for instrument in self.__instruments:
        
            bar = bars[instrument]   

            
            if bar.getClose() == 8.79 and str(instrument) == "000001.SZ":
                
                #订单可部分完成，默认是createMarketOrder
                self.__position = self.enterLong(instrument, 100,True) #美股买卖最小单位为股，需要做input合法性判断
                print str(instrument) + " buy in 100 shares"
              
            if bar.getClose() == 8.81 and str(instrument) == "000001.SZ":
                self.__position == self.enterShort(instrument,100,True)
                print str(instrument) + " sell out 100 shares"
           
            if bar.getClose() == 19.19 and str(instrument) == "000002.SZ":
                self.__position = self.enterLong(instrument, 200,True) #
                print str(instrument) + " buy in 200 shares"
        

        print "\n"
          
                  
feed = windfeed.Feed()
feed.addBarsFromCSV("000001.SZ", "dataFile/000001.SZ.csv")
feed.addBarsFromCSV("000002.SZ", "dataFile/000002.SZ.csv")

instruments = ["000001.SZ", "000002.SZ"]

myStrategy = MyStrategy(feed,instruments)


retAnalyzer = returns.Returns()
myStrategy.attachAnalyzer(retAnalyzer)
drawDownAnalyzer = drawdown.DrawDown()
myStrategy.attachAnalyzer(drawDownAnalyzer)
sharpeRatioAnalyzer = sharpe.SharpeRatio()
myStrategy.attachAnalyzer(sharpeRatioAnalyzer)


myStrategy.run()


    #夏普率
sharp = sharpeRatioAnalyzer.getSharpeRatio(0.05)
    #最大回撤
maxdd = drawDownAnalyzer.getMaxDrawDown()
    #收益率
return_ = retAnalyzer.getCumulativeReturns()[-1]
    #收益曲线


print "sharp ratio is " +str(sharp)
print "maxdd is " + str(maxdd)
print "return is" + str(return_)




