import json as js
from time import strftime
import time 
import threading
import baostock as bs
import pandas as pd
import os 
import matplotlib.pyplot as plt
import datetime as dt
import pymysql
from sqlalchemy import create_engine

def get_all_stock(tmp):
    bs.login()
    source = bs.query_all_stock(day=tmp)
    db_list=[]
    while (source.error_code=='0')& source.next():
        db_list.append(source.get_row_data())
    global res
    res = pd.DataFrame(db_list,columns=source.fields)
    res.to_json('json.equ',force_ascii=False)
    bs.logout()

def using_json():
    txt = open('json.equ','r',encoding='utf-8')
    global obj
    obj = js.loads(txt.read())
    txt.close()

def create_new_dir_source():
    test = os.path.exists('equity')
    if not test:
        os.makedirs('equity')
        for i in range(len(res) - 1):
            test_dir  = os.path.exists('equity/'+obj['code'][str(i)])
            if not test_dir:
                os.makedirs('equity/'+obj['code'][str(i)])

def create_new_source_in_dirs(tmp_o,tmp_n):
    bs.login()
    for i in range(len(res) - 1 ):
        fields="date,close,volume,turn,peTTM"
        rs = bs.query_history_k_data(obj['code'][str(i)],fields,start_date=tmp_o,end_date=tmp_n,frequency="d", adjustflag="2")
        data_list=[]
        while (rs.error_code == '0') & rs.next():
            data_list.append(rs.get_row_data())
        result = pd.DataFrame(data_list, columns=rs.fields)
        engine = create_engine('mysql+pymysql://source:equity@localhost:3306/source?charset=utf8')
        result.to_sql(obj['code'][str(i)],con=engine,if_exists='replace')

        result.index=pd.to_datetime(result.date)
        result.to_json('equity/'+obj['code'][str(i)]+'/'+obj['code'][str(i)]+'.equ',force_ascii=False,orient='records')
        result.head()
        result.info()
        result=result.apply(pd.to_numeric, errors='ignore')
        result.info()
        c = result.close.mean()
        result['equit']= c
        u = result.volume.mean()
        result['equit1']= u
        p = result.turn.mean()
        result['equit2']= p
        l = result.peTTM.mean()
        result['equit3']= l

        result.close.plot(figsize=(16,8))
        result.equit.plot(figsize=(16,8))
        ax = plt.gca()  
        ax.spines['right'].set_color('none') 
        ax.spines['top'].set_color('none')    
        plt.savefig('equity/'+obj['code'][str(i)]+'/'+'close.png',dpi=300)
        plt.clf()
        plt.cla()

        result.volume.plot(figsize=(16,8))
        result.equit1.plot(figsize=(16,8))
        ax = plt.gca()  
        ax.spines['right'].set_color('none') 
        ax.spines['top'].set_color('none')    
        plt.savefig('equity/'+obj['code'][str(i)]+'/'+'volume.png',dpi=300)
        plt.clf()
        plt.cla()

        result.turn.plot(figsize=(16,8))
        result.equit2.plot(figsize=(16,8))
        ax = plt.gca()  
        ax.spines['right'].set_color('none') 
        ax.spines['top'].set_color('none')    
        plt.savefig('equity/'+obj['code'][str(i)]+'/'+'turn.png',dpi=300)
        plt.clf()
        plt.cla()

        result.peTTM.plot(figsize=(16,8))
        result.equit3.plot(figsize=(16,8))
        ax = plt.gca()  
        ax.spines['right'].set_color('none') 
        ax.spines['top'].set_color('none')    
        plt.savefig('equity/'+obj['code'][str(i)]+'/'+'TTM.png',dpi=300)
        plt.clf()
        plt.cla()
        print(obj['code'][str(i)]+' done')
    bs.logout()

def writeee():
    today = dt.date.today()
    wkd = today.weekday
    de = dt.timedelta(days=31)
    ye = today-de
    if wkd != 6 or wkd != 0:
        get_all_stock(today.strftime('%Y-%m-%d'))
        using_json()
        create_new_dir_source()
        create_new_source_in_dirs(ye.strftime('%Y-%m-%d'),today.strftime('%Y-%m-%d'))
    else:
        print('weeknd')

def timeseting():
    tm_str = time.strftime("%H-%M", time.localtime())
    if tm_str=='20-00':
        writeee()
    threading.Timer(60,timeseting)
timeseting()

writeee()