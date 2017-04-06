#!/usr/bin/python env
#coding=utf-8

import tushare as ts
import pandas
import PolicyOne

def getTradeData(code, date):
    df = ts.get_tick_data(code, date=date)
    print df

if __name__ == "__main__":
    df = PolicyOne.TradeGetDDBuy('600848', '2017-03-24', 100)
    print df
