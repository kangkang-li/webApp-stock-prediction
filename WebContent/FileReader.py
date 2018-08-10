# written by: KangKang.Li
# assisted by: Lang.Liu
# debugged by: Jiawen.Sun Mingbo.Zhang
# import util
import sys
import json
from os import path
# import numpy as np
# import tensorflow as tf

batch_size = 20
#batch_len = 8

def _read_file(path, tag):
    js_data = json.load(open(path))
    dkey = "Time Series (Daily)"
    out = []
    if dkey in js_data:
        for key, val in js_data[dkey].items():
            out.insert(0,float(val[tag]))
            
    
    #norm_out = out    
    return out

def readCSV(filename,dataType,date,n):
    if dataType==0:#open
        dataType=3
    elif dataType==1:#high
        dataType=4
    elif dataType==2:#high
        dataType=5
    elif dataType==3:#high
        dataType=1
    d = path.dirname(path.dirname(path.dirname(__file__)))
    # print(d)
    with open(d+'//dataset//daily//'+filename+'.csv', 'r') as file:
        file.readline()
        # file.readline()
        csv_file = csv.reader(file)
        # print(csv_file[0])
        # for row in csv_file:
            # print(row[1])
            # print(row)
        dataSource=[float(row[dataType].replace(',','')) for row in csv_file]
    # dataSource=[float(i) for i in dataSource[1:]]
    # trueValue=dataSource[pointStart-1]
    # dataTrain=dataSource[pointStart-n:pointStart]
    # dataTrain=[]
    # print(dataSource)
    # print(len(dataSource))
    return dataSource
def readJson(filename,n,isDaily):
    # '1. open': '970.0000', '2. high': '981.5100', '3. low': '969.6400', '4. close': '980.8500'
    
    dataType=['1. open','2. high', '3. low', '4. close']
    # dataType=0
    # if dataType==0:#open
    #     dataType='1. open'
    # elif dataType==1:#high
    #     dataType='2. high'
    # elif dataType==2:#high
    #     dataType='3. low'
    # elif dataType==3:#high
    #     dataType=1
    # d = path.dirname(path.dirname(path.dirname(__file__)))
    d2=''
    # print(d2)
    dkey=''
    if isDaily:
        d2=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\'+filename+'.json'
        
        dkey = 'Time Series (Daily)'
    else:
        d2=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\intraday\\'+filename+'.json'
        dkey ='Time Series (1min)'
    # print(d)
    # print(_read_file(d,dataType))
    js_data = json.load(open(d2))
    # print(type(js_data))
    result=[]
    counter=0
    if dkey in js_data:
        if n >0:
            n=min(n,len(js_data[dkey]))
        else:
            n=len(js_data[dkey])
        result=[[0]*n,[0]*n,[0]*n,[0]*n,[0]*n]
        for key, val in js_data[dkey].items():
            for j in range(4):
                v=(float(val[dataType[j]]))
                # print(v,counter,j)
                result[j][counter]=(float(val[dataType[j]]))
            result[4][counter]=key
            counter+=1
            if counter==n:
                break
    # print(js_data)
    # print(result)
    return result
    # for item in result:
        # print(item)
# print(readJson('AMZN',10,True))
