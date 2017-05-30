# -*- coding: utf-8 -*-
"""
Created on Wed May 24 09:47:39 2017

@author: Think
"""
from pyalgotrade import strategy
from pyalgotrade.barfeed import windfeed
from pyalgotrade.barfeed import yahoofeed
from pyalgotrade.technical import ma
from pyalgotrade import plotter
from pyalgotrade.technical import cross

from pyalgotrade.stratanalyzer import returns
from pyalgotrade.stratanalyzer import sharpe
from pyalgotrade.stratanalyzer import drawdown
from pyalgotrade.stratanalyzer import trades

class SMACrossOver(strategy.BacktestingStrategy):
    def __init__(self,feed,instrument,smaPeriod):
        strategy.BacktestingStrategy.__init__(self,feed)
        self.__position = None
        self.__instrument = instrument
        self.setUseAdjustedValues(True)
        
        self.__prices = feed[instrument].getPriceDataSeries()
        self.__sma = ma.SMA(self.__prices, smaPeriod)
 
    
        
        #self.setUseAdjustedValues(True)
        #self.__sma = ma.SMA(feed[instrument].getPriceDataSeries(),smaPeriod)
    def getSMA(self):
        return self.__sma
        
    def onEnterOk(self,position):
        #execInfo = position.getEntryOrder().getExecutionInfo()
        #self.info("BUY at %.2f" %(execInfo.getPrice()))
        pass
    
    def onEnterCanceled(self,position):
        self.__position = None
        
    def doExitOk(self,position):
        #execInfo = position.getEntryOrder().getExecutionInfo()
        #self.info("SELL at %.2f" %(execInfo.getPrice()))
        self.__position = None
        
    def onExitCanceled(self,position):
        self.__position.exitMarket()
        
    def onBars(self,bars):
        
        if self.__position is None:
            if cross.cross_above(self.__prices,self.__sma)>0:
                shares = int(self.getBroker().getCash()*0.9/bars[self.__instrument].getPrice())
                self.__position = self.enterLong(self.__instrument,shares, True)
                print "buy"
                print bars[self.__instrument].getDateTime(), bars[self.__instrument].getPrice()
        elif not self.__position.exitActive() and cross.cross_below(self.__prices,self.__sma) >0:
                self.__position.exitMarket()
                print "sell"
                print bars[self.__instrument].getDateTime(), bars[self.__instrument].getPrice()
        """
        if self.__ma2[-1] is None:
            return
        
        bar = bars[self.__instrument]
        
               #平仓
        if self.__position is not None:
            if not self.__position.exitActive() and cross.cross_below(self.__ma1, self.__ma2) > 0:
                self.__position.exitMarket()
                print "sell"
                print bar.getDateTime(), bar.getPrice()
        
        #开仓
        if self.__position is None:
            if cross.cross_above(self.__ma1, self.__ma2) > 0:
                shares = int(self.getBroker().getEquity() / bars[self.__instrument].getPrice())
                self.__position = self.enterLong(self.__instrument, shares)
                #print bars[self.__instrument].getDateTime(), bars[self.__instrument].getPrice()
                #self.info("buy %s" % (bars.getDateTime()))
                print "buy"
                print bar.getDateTime(), bar.getPrice()
        """
        
        
            
def run_strategy(m):
    
    feed = yahoofeed.Feed()
    feed.addBarsFromCSV("test1","../dataFile/orcl-2000.csv")
    
    myStrategy = SMACrossOver(feed,"test1",m)
    
    
    retAnalyzer = returns.Returns()
    myStrategy.attachAnalyzer(retAnalyzer)
    drawDownAnalyzer = drawdown.DrawDown()
    myStrategy.attachAnalyzer(drawDownAnalyzer)
    tradesAnalyzer = trades.Trades()
    myStrategy.attachAnalyzer(tradesAnalyzer)
    
    
    myStrategy.run()
    
    print "total trades: %d" %(tradesAnalyzer.getCount())
    
    """
    plot = True
    
    plt = plotter.StrategyPlotter(myStrategy, True, True, True)
    
    myStrategy.run()
    
    if plot:
        plt.plot()
    
    print "Final portfolio value: %.2f" %myStrategy.getBroker().getEquity()
    """
run_strategy(20)

        
        
        
        
        
        
        
        
        
        

