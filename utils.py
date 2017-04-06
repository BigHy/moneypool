#!/usr/bin/python env
#coding=utf-8

import tushare as ts
import pandas
import PolicyOne

def getTradeData(code, date):
    df = ts.get_tick_data(code, date=date)
    print df

if __name__ == "__main__":
    df_buy = PolicyOne.TradeGetAllBuy('600848', '2017-03-24')
    avg_amout_buy = sum(df_buy["volume"])/len(df_buy["volume"])
    avg_buy = sum(df_buy["price"])/len(df_buy["price"])

    df_sell = PolicyOne.TradeGetAllSell('600848', '2017-03-24')
    avg_sell = sum(df_sell["price"])/len(df_sell["price"])
    avg_amount_sell = sum(df_sell["volume"])/len(df_sell["volume"])
    print avg_buy, avg_amout_buy
    print avg_sell, avg_amount_sell
