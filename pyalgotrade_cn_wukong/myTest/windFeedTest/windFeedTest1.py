# -*- coding: utf-8 -*-
"""
Created on Tue May 23 14:03:11 2017

@author: Think
"""
from pyalgotrade import strategy
from pyalgotrade.barfeed import windfeed

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed,instruments):
        strategy.BacktestingStrategy.__init__(self,feed)
        self.__instruments = instruments
        
    def onBars(self,bars):
        
        for instrument in self.__instruments:
            bar = bars[instrument]
            self.info(bar.getClose())
        print "end!"
        
feed = windfeed.Feed()
feed.addBarsFromCSV("test1","../dataFile/000001.SZ.csv")
feed.addBarsFromCSV("test2","../dataFile/000002.SZ.csv")
feed.addBarsFromCSV("test3","../dataFile/000004.SZ.csv")
feed.addBarsFromCSV("test4","../dataFile/000005.SZ.csv")
        
instruments = ["test1","test2","test3","test4"]

myStrategy = MyStrategy(feed,instruments)
myStrategy.run()
        
        
    


