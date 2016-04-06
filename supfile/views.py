# -*- coding: utf-8 -*-

'''获取当前日期前后N天或N月的日期'''

from time import  localtime, strftime
from datetime import timedelta, date
import calendar

year = strftime("%Y",localtime())
mon  = strftime("%m",localtime())
day  = strftime("%d",localtime())

def today():
    '''''
    get today,date format="YYYY-MM-DD"
    '''''
    return year + "-" + mon + "-" + day

def nextday(n=0):
    '''''
    if n>=0,date is larger than today
    if n<0,date is less than today
    date format = "YYYY-MM-DD"
    '''
    if(n<0):
        n = abs(n)
        nextday = date.today()-timedelta(days=n)
    else:
        nextday = date.today()+timedelta(days=n)
    next_year = str(nextday.year)
    next_mon  = str(nextday.month)
    next_day  = str(nextday.day)
    if(nextday.month < 10) :
        #print next_mon
        next_mon 	= "0" + next_mon
    if(nextday.day < 10) :
        next_day 	= "0" + str(next_day)

    return next_year + "-" + next_mon + "-" + next_day
