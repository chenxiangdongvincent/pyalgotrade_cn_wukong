# -*- coding: utf-8 -*-
"""
Created on Sat May 20 15:41:50 2017

@author: Think
"""

from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed,instrument):
        strategy.BacktestingStrategy.__init__(self,feed)
        self.__instrument = instrument
   
    def onBars(self,bars):
        bar = bars[self.__instrument]
        self.info(bar.getClose())
    
        
feed = yahoofeed.Feed()
feed.addBarsFromCSV("orcl", "orcl-2000.csv")

myStrategy = MyStrategy(feed,"orcl")
myStrategy.run()