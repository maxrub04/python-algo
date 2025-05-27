import backtrader as bt
import datetime

class SMA_CrossOver(bt.Strategy):
    params = (('period', 15), ('sma_period', 20), ('printlog', False),)