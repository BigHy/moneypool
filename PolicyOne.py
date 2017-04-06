#!/usr/bin/python env
#coding=utf-8
import pandas
import tushare as ts
from utils import getTradeData

def TradeSortByAmount(code ,date):
    df = ts.get_tick_data(code, date)
    df.sort(columns='amount')
    return df

def TradeSortByVolume(code, date):
    df = ts.get_tick_data(code, date)
    print df.sort(columns='volume')
    return df

def TradeGetAllBuy(code, date):
    df = ts.get_tick_data(code, date)
    df2 = df.copy()
    alist = ['买盘']
    return df[df2['type'].isin(alist)]

def TradeGetAllSell(code, date):
    df = ts.get_tick_data(code, date)
    df2 = df.copy()
    alist = ['卖盘']
    return df[df2['type'].isin(alist)]

def TradeGetDDBuy(code, date, volume):
    df = ts.get_sina_dd(code, date=date ,vol=volume)
    df2 = df.copy()
    alist = ['买盘']
    return df[df2['type'].isin(alist)]

def TradeGetDDSell(code, date, volume):
    df = ts.get_sina_dd(code, date=date ,vol=volume)
    df2 = df.copy()
    alist = ['卖盘']
    return df[df2['type'].isin(alist)]


