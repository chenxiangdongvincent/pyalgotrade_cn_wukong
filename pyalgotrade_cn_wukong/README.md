### 2016-09-03 ���£�
1. �ϲ����б��ػ���ģ�鵽/cn�ļ����У�������ʹ�ú͸�ԭ����жԱȡ�
2. pyalgotrade��������Ϊ0.18.
3. �����tick����ṹ��֧�֣���/stratlib/orderbook.py


Pyalgotrade-cn ��ԭ��Ļ����ϼ�����A����ʷ����ز⣬��������tushare�ṩʵʱ���顣�Ա��Ҷ��Լ��Ĳ��Խ��лز��ģ����ԡ�

���θ��µ����ݣ�

 * ����tushareʵʱ����
 * stratlib�ṩ�������������(DT, Bollinger_bandit)

��ʷ�������أ�������󣬲μ����ۣ����Ⱥ��300349971


������ԭ��Ľ��ܣ�

PyAlgoTrade is an **event driven algorithmic trading** Python library. Although the initial focus
was on **backtesting**, **paper trading** is now possible using:

 * [Bitstamp](https://www.bitstamp.net/) for Bitcoins
 * [Xignite](https://www.xignite.com/) for stocks

and **live trading** is now possible using:

 * [Bitstamp](https://www.bitstamp.net/) for Bitcoins

To get started with PyAlgoTrade take a look at the [tutorial](http://gbeced.github.io/pyalgotrade/docs/v0.17/html/tutorial.html) and the [full documentation](http://gbeced.github.io/pyalgotrade/docs/v0.17/html/index.html).

Main Features
-------------

 * Event driven.
 * Supports Market, Limit, Stop and StopLimit orders.
 * Supports any type of time-series data in CSV format like Yahoo! Finance, Google Finance, Quandl and NinjaTrader.
 * [Xignite](https://www.xignite.com/) realtime feed.
 * Bitcoin trading support through [Bitstamp](https://www.bitstamp.net/).
 * Technical indicators and filters like SMA, WMA, EMA, RSI, Bollinger Bands, Hurst exponent and others.
 * Performance metrics like Sharpe ratio and drawdown analysis.
 * Handling Twitter events in realtime.
 * Event profiler.
 * TA-Lib integration.

Installation
------------

PyAlgoTrade is developed using Python 2.7 and depends on:

 * [NumPy and SciPy](http://numpy.scipy.org/).
 * [pytz](http://pytz.sourceforge.net/).
 * [dateutil](https://dateutil.readthedocs.org/en/latest/).
 * [requests](http://docs.python-requests.org/en/latest/).
 * [matplotlib](http://matplotlib.sourceforge.net/) for plotting support.
 * [ws4py](https://github.com/Lawouach/WebSocket-for-Python) for Bitstamp support.
 * [tornado](http://www.tornadoweb.org/en/stable/) for Bitstamp support.
 * [tweepy](https://github.com/tweepy/tweepy) for Twitter support.

You can install PyAlgoTrade using pip like this:

```
pip install pyalgotrade
```
