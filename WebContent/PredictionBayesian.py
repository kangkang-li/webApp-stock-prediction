# written by: KangKang.Li
# assisted by: Lang.Liu
# debugged by: Jiawen.Sun Mingbo.Zhang

import statistics
import numpy as np
import math
# import csv
# import os
from FileReader import readJson
from os import path
import json
import sys
import ctypes
# KangKang Li, kl689

def bayesian(data,M,N):
    # x_n = []
    x_n = list(range(1,N+1))
    # t_data = []
    t_data =data[:N]

    # for i in range(len(data) - N, len(data)):
        # t_data.append(data[i])
    # for i in range(1, N+1):
        # x_n.append(i)
    t = []
    t.append(t_data)
    t_data = t
    rel_err_dr = 0
    x = x_n[len(x_n) - 1] + 1
    for k in range(1):
        t = np.zeros((N, 1), float)
        phi = np.zeros((M, 1), float)
        phi_sum = np.zeros((M, 1), float)
        phi_sum_t = np.zeros((M, 1), float)
        for i in range(M):
            phi[i][0] = math.pow(x,i)
        for i in range(N):
            t[i][0] = t_data[k][i]
        for j in range(N):
            for i in range(M):
                phi_sum[i][0] = phi_sum[i][0] + math.pow(x_n[j],i)
                phi_sum_t[i][0] = phi_sum_t[i][0] + t[j][0] * math.pow(x_n[j],i)

    # ''' Calculation of variance / standard deviation '''
        S = np.linalg.inv(0.005 * np.identity(M) + 11.1 * np.dot(phi_sum, phi.T))
        var = np.dot((phi.T), np.dot(S,phi))
        var = var + 1 / 11.1
    # ''' Calculating the mean '''
        mean = 11.1 * np.dot(phi.T, np.dot(S,phi_sum_t))
        mean = mean[0][0]
        # print ('mean', mean)
    t = t_data[0]
    t_data = t
    sum = 0
    avg = 0
    # print ('t_data', t_data)
    for i in t_data:
        sum = sum + float(i)
    mov = sum / len(t_data)
    # print ('mov', mov)
    per = ((mean - mov) / mov) * 100
    # print ('per', per)
    final = []
    mean = round(mean, 3)
    per =   round(per, 3)
    final.append(mean)
    # final.append(per)
    return mean

# data size for training n=10
# highest M=6

# if __name__ == "__main__":
def bayesianCaller(stockSymbol,isDaily=True):
    n=20
    m=6
    date=0
    # fileArray=['NFLX.csv', 'NVDA.csv', 'TESL.csv', 'WB.csv']
    # dataSource=readCSV(stockSymbol,dataType,date,n)
    dataTrain=readJson(stockSymbol,n,isDaily)

    # readCSV(stockSymbol,dataType,date,n)
    # if date<0 or date+n>=len(dataSource):
        # return [-2,-2,-2]
    # print(dataTrain)
    if date+n>len(dataTrain[0]):
        return ([-2,-2,-2,-2],-2,-2)
    # dataTrain=dataSource[date:date+n][::-1]
    # for n in [6,10,16,20]:
        # print('n='+str(n))
        # for m in [5,6,7,8]:
            # print('n='+str(n)+', m='+str(m))
            # result=[]
            # avgRelErr=0
            # for stockSymbol in fileArray:
                # for pointStart in [1,101,201]:
    prediction=[0]*4
    for i in range(4):
        # print(dataTrain[i])
        prediction[i] = round(bayesian(dataTrain[i],m,n),2)
    # print(dataTrain)
    stdev=round(statistics.stdev(dataTrain[3]),2)
    averageErrorPath=''
    if isDaily:
        #ctypes.windll.user32.MessageBoxW(0, path.abspath(path.join(path.abspath(sys.argv[0]), "..")), "Your title", 1)
        averageErrorPath=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_averageErr_bayesian.json'
    else:
        #ctypes.windll.user32.MessageBoxW(0, path.abspath(path.join(path.abspath(sys.argv[0]), "..")), "Your title", 1)
        averageErrorPath=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\intraday\\prediction_averageErr_bayesian.json'

    with open(averageErrorPath,'r') as f:
        averageError=json.load(f)[stockSymbol]

    # print(prediction)

    return(prediction[0],prediction[1],prediction[2],prediction[3],averageError,stdev)
                    # avgRelErr+=abs((trueValue-prediction)/trueValue*100)
                    # result.append(['%.2f' % trueValue, '%.2f' %prediction, '%.2f' %(trueValue-prediction), '%.2f%%' % abs((trueValue-prediction)/trueValue*100)])
                    # print(dataTrain)
                    # print (prediction)
            # for singleTest in result:
            #     for num in singleTest:
            #         print (num,end='')
            #         print (", ", end='')
            #     print()
            # print("average relative error="+str('%.2f%%' %(avgRelErr/12)))

def bayesianHistory(stockSymbol,dateScope,gap,isDaily=True):
    m=6
    n=gap
    dataSource=readJson(stockSymbol,-1,isDaily)[3:5] #price close only
    # print(dataSource)
    # readCSV(stockSymbol,dataType,date,n)
    # if date<0 or date+n>=len(dataSource):
        # return [-2,-2,-2]
    if dateScope>=len(dataSource[0]):
        return -1
    errorSum=0
    result={}
    prediction =bayesian(dataSource[0][9::-1],m,n)
    result['nextDay']={}
    result['nextDay']['prediction']=prediction
    for k in range(gap,dateScope-gap,gap):
        dataTrain=dataSource[0][k:k+gap][::-1]
        trueValue=dataSource[0][k-1]
        date=dataSource[1][k-1]
        prediction =bayesian(dataTrain,m,n)
        error=abs((prediction-trueValue)/trueValue*100)
        result[date]={}
        result[date]['prediction']=prediction
        result[date]['trueValue']=trueValue
        result[date]['relativeError']=error
        errorSum+=error
    # for n in [6,10,16,20]:
        # print('n='+str(n))
        # for m in [5,6,7,8]:
            # print('n='+str(n)+', m='+str(m))
            # result=[]
            # avgRelErr=0
            # for stockSymbol in fileArray:
                # for pointStart in [1,101,201]:
    # prediction=[0]*4
    # for i in range(4):
    #     prediction[i] = round(bayesian(dataTrain[i],m,n),2)
    # # print(dataTrain)
    # stdev=round(statistics.stdev(dataTrain[3]),2)
    # # print(prediction)
    # return(prediction,-1,stdev)
    # print (result)
    averageError=errorSum/len(result)
    # print(averageError)
    curvefile=''
    avgFile=''
    
    if isDaily:
        curvefile='dataset/daily/prediction_'+stockSymbol+'_bayesian.json'
        avgFile='dataset/daily/prediction_averageErr_bayesian.json'
    else:
        curvefile='dataset/intraday/prediction_'+stockSymbol+'_bayesian.json'
        avgFile='dataset/intraday/prediction_averageErr_bayesian.json'
    # print(result)
    with open(curvefile,"w") as f:
        json.dump(result,f)

    with open(avgFile,"r") as f:
        # errStr=json.load(f)
        errDict = json.load(f)
        errDict[stockSymbol]=averageError
    with open(avgFile,"w") as f:
        json.dump(errDict,f)

if __name__ == "__main__":
#     # d = path.dirname(__file__)
#     # d=path.dirname(d)
#     # print(path.dirname(path.dirname(path.dirname(__file__))))
    # print(bayesianCaller('AMZN'))
    bayesianHistory('AMZN',500,10,isDaily=True)