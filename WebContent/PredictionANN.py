# written by: KangKang.Li
# assisted by: Lang.Liu
# debugged by: Jiawen.Sun Mingbo.Zhang
# coding=utf-8
import statistics
import math
import numpy as np
import random
from FileReader import readJson
import json
import sys
import os
from os import path

# random.seed(0)

stock=''
def rand(a, b):
    """
    创建一个满足 a <= rand < b 的随机数
    :param a:
    :param b:
    :return:
    """
    return (b - a) * random.random() + a


def makeMatrix(I, J, fill=0.0):
    """
    创建一个矩阵（可以考虑用NumPy来加速）
    :param I: 行数
    :param J: 列数
    :param fill: 填充元素的值
    :return:
    """
    m = []
    for i in range(I):
        m.append([fill] * J)
    return m


def randomizeMatrix(matrix, a, b):
    """
    随机初始化矩阵
    :param matrix:
    :param a:
    :param b:
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # matrix[i][j] = random.uniform(a, b)
            matrix[i][j] = 0.1
def tanh(x):
    return np.tanh(x)

def dthanh(x):
    return 1.0 - np.tanh(x) ** 2

def reLU(x):
    return x * (x > 0)

def dReLU(x):
    return 1 * (x > 0)

def sigmoid(x):
    """
    sigmoid 函数，1/(1+e^-x)
    :param x:
    :return:
    """
    return 1.0 / (1.0 + math.exp(-x))


def dsigmoid(y):
    """
    sigmoid 函数的导数
    :param y:
    :return:
    """
    return y * (1 - y)

def activation(x):
    return reLU(x)
def dActivation(y):
    return dReLU(y)

class NN:
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        """
        构造神经网络
        :param ni:输入单元数量
        :param nh:隐藏单元数量
        :param no:输出单元数量
        """
        self.ni = ni
        self.nh = nh
        self.no = no

        # 激活值（输出值）
        self.ai = [1.0] * self.ni
        self.ah = [1.0] * self.nh
        self.ao = [1.0] * self.no

        # 权重矩阵
        self.wi = makeMatrix(self.ni, self.nh)  # 输入层到隐藏层
        self.wo = makeMatrix(self.nh, self.no)  # 隐藏层到输出层

        

        # 权重矩阵的上次梯度
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)
        # self.weights()
    def loadWeights(self,stockSymbol):
        itemDict={}
        with open(path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_ANN_weights.json',"r") as f:
            itemDict=json.load(f)[stockSymbol]

        self.wi=itemDict['layer1']
        self.wo=itemDict['layer2']
        # print(self.wi)
        # print(self.wo)

    def initWeightsRand(self):
        randomizeMatrix(self.wi, -1, 1)
        randomizeMatrix(self.wo, -1, 1)

    def runNN(self, inputs):
        """
        前向传播进行分类
        :param inputs:输入
        :return:类别
        """
        if len(inputs) != self.ni - 1:
            print ('incorrect number of inputs')
            return
        for i in range(self.ni - 1):
            self.ai[i] = inputs[i]

        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum += ( self.ai[i] * self.wi[i][j] )
            self.ah[j] = activation(sum)

        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum += ( self.ah[j] * self.wo[j][k] )
            self.ao[k] = activation(sum)
        # print(self.ao)
        return self.ao


    def backPropagate(self, targets, N, M):

        # 计算输出层 deltas
        # dE/dw[j][k] = (t[k] - ao[k]) * s'( SUM( w[j][k]*ah[j] ) ) * ah[j]
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k] - self.ao[k]
            output_deltas[k] = error * dActivation(self.ao[k])

        # 更新输出层权值
        for j in range(self.nh):
            for k in range(self.no):
                # output_deltas[k] * self.ah[j] 才是 dError/dweight[j][k]
                change = output_deltas[k] * self.ah[j]
                self.wo[j][k] += N * change + M * self.co[j][k]
                self.co[j][k] = change

        # 计算隐藏层 deltas
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error += output_deltas[k] * self.wo[j][k]
            hidden_deltas[j] = error * dActivation(self.ah[j])

        # 更新输入层权值
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j] * self.ai[i]
                # print 'activation',self.ai[i],'synapse',i,j,'change',change
                self.wi[i][j] += N * change + M * self.ci[i][j]
                self.ci[i][j] = change

        # 计算误差平方和
        # 1/2 是为了好看，**2 是平方
        error = 0.0
        for k in range(len(targets)):
            error += 0.5 * (targets[k] - self.ao[k]) ** 2
        return error


    def printWeights(self):
        print('  1st layer, 3*3 including a constant and two x:',end='')
        for item in self.wi:
            print(['%0.2f' %weight for weight in item],end='')
        print()

        print('  2st layer:',end='')
        for item in self.wo:
            print(['%0.2f' %weight for weight in item],end='')
        print()

    def saveWeightJson(self,isDaily=True):
        # weightDict={}
        # weightDict[layer1]=
        # keys=['BABA','BIDU','FB','GOOGL','JD','MSFT','NVDA','TSLA','WB']

        if isDaily:
            curvefile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_'+stock+'_ANN.json'
            avgFile='..//..//dataset//daily//prediction_averageErr_ANN.json'
        else:
            curvefile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\intraday\\prediction_'+stock+'_ANN.json'
            avgFile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\intraday\\prediction_averageErr_ANN.json'

        mainDict={}
        itemDict={}
        # d[1]=[1,2,3]

        with open(path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_ANN_weights.json',"r") as f:
            mainDict=json.load(f)
        weightsArray1=[]
        weightsArray2=[]
        mainDict[stock]=itemDict
        for item in self.wi:
            weightsArray1.append(item)
        for item in self.wo:
            weightsArray2.append(item)
        itemDict['layer1']=weightsArray1
        itemDict['layer2']=weightsArray2
        print(mainDict)
        with open(path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_ANN_weights.json',"w") as f:
            json.dump(mainDict,f)
        # with open(curvefile,"w") as f:
        #     json.dump(result,f)


        # for item in self.wi:
        #     print(['%0.2f' %weight for weight in item],end='')
        # print()

        # print('  2st layer:',end='')
        # for item in self.wo:
        #     print(['%0.2f' %weight for weight in item],end='')
        # print()
    def updateHistory(self,isDaily=True):
        # weightDict={}
        # weightDict[layer1]=
        # keys=['BABA','BIDU','FB','GOOGL','JD','MSFT','NVDA','TSLA','WB']

        if isDaily:
            curvefile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_'+stock+'_ANN.json'
            avgFile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_averageErr_ANN.json'
        else:
            curvefile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\intraday\\prediction_'+stock+'_ANN.json'
            avgFile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\intraday\\prediction_averageErr_ANN.json'

        mainDict={}
        itemDict={}
        # d[1]=[1,2,3]

        with open(path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_ANNweights.json',"r") as f:
            mainDict=json.load(f)
        weightsArray1=[]
        weightsArray2=[]
        mainDict[stock]=itemDict
        for item in self.wi:
            weightsArray1.append(item)
        for item in self.wo:
            weightsArray2.append(item)
        itemDict['layer1']=weightsArray1
        itemDict['layer2']=weightsArray2
        print(mainDict)
        with open(path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_ANNweights.json',"w") as f:
            json.dump(mainDict,f)

    def test(self, patterns):
        """
        测试
        :param patterns:测试数据
        """
        for p in patterns:
            inputs = p[0]
            print ('Inputs:', p[0], '-->', '%0.3f'% self.runNN(inputs)[0], '\tTarget', p[1])

    def train(self, patterns,errorRequirement,doesPrint, max_iterations=10000, N=0.7, M=0):
        roundCounter=0
        error=1
        if doesPrint:
            print('(2)the first-batch error:',end='')
            error = 0.0
            Y=[item[1][0]for item in patterns]
            predicts=[]
            # for item in patterns:
            predicts=[self.runNN(item[0])[0] for item in patterns ]
            # print(Y)
            # print(predicts)
            for k in range(len(Y)):
                error += 0.5 * (Y[k] - predicts[k]) ** 2
            # print('%0.2f'%error)
        roundError=4
        while roundError>errorRequirement:
            roundError=0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.runNN(inputs)
                error = self.backPropagate(targets, N, M)
                roundError+=error
            roundError/=4
            roundCounter+=1
            if roundCounter>max_iterations:
                # print('round>',max_iterations,'return')
                # return roundCounter
                break
            # print(error)
        # return

        # self.test(patterns)
        if doesPrint:
            print('(3) the final weights:')
            self.printWeights()
            print('(4) the final error:','%0.4f'%roundError)
            self.test(patterns)
            # print('(5) the total number of batches run through in the training:',roundCounter)
        return roundCounter


def predictANN(errorRequirement,learningRate):
    # print('errorRequirement=',errorRequirement, '  learningRate=', learningRate)

    roundKeeper=[]
    pat = [
        [[0, 0], [0]],
        [[0, 1], [1]],
        [[1, 0], [1]],
        [[1, 1], [0]]
    ]
    myNN = NN(3, 3, 1)
    # print('(1) the initial weights:')
    myNN.printWeights()
    roundKeeper.append(myNN.train(pat,errorRequirement,True,N=learningRate))
    # for i in range(10):
    #     myNN = NN(3, 3, 1)
    #     roundKeeper.append(myNN.train(pat,errorRequirement,False,N=learningRate))
    

    # print('10 parallel test:',roundKeeper,'average:',int(sum(roundKeeper)/10))
    # print()
def dataFormatter(dataSource,gap,quantity,datalen):
    result=[]
    # print(len(dataSource))
    # print(datalen)
    for i in range(0,datalen-gap,gap):
        result.append([dataSource[i:i+gap],[dataSource[i+gap]]])
    return(result)
def callerANN(stockSymbol,isDaily=True):
    dataSource=readJson(stockSymbol,61,isDaily)
    # print(dataSource)
    global stock
    stock=stockSymbol

    result=[]
    # prediction=[0]*4
    # print(dataSource[3][10:])
    dataTrain=dataFormatter(dataSource[3][10:][::-1],10,5,51)[::-1]
    dateArray=[]
    for num in [10,20,30,40,50]:
        dateArray.append(dataSource[4][num])
    # print(dateArray)

    # print(dataTrain)

    myNN = NN(11, 5, 1)
    # myNN.initWeightsRand()
    myNN.loadWeights()
    for inputData,outputData in dataTrain:
        predictionItem=myNN.runNN(inputData)
        print(inputData,outputData,predictionItem)

    # myNN.train(dataTrain,1,True,N=0.00000001)
    # myNN.saveWeightJson()
        # prediction[i] = round(predictANN(dataTrain[i],errorRequirement,learningRate),2)
def testANN(stockSymbol,isDaily=True):
    dataSource=readJson(stockSymbol,250,isDaily)
    # print(dataSource)
    global stock
    stock=stockSymbol
    myNN = NN(11, 5, 1)
    # myNN.initWeightsRand()
    myNN.loadWeights(stockSymbol)


    result=[]
    resultJson={}
    resultJson[stockSymbol]={}

    # prediction=[0]*4
    # print(dataSource[3][10:])
    dataTrain=dataFormatter(dataSource[3][9:][::-1],10,5,241)[::-1]
    # print(len(dataTrain))
    dateArray=[]
    for num in range(10,241,10):
        dateArray.append(dataSource[4][num])


    errorSum=0
    result={}
    # print(dataSource[3][:10][::-1])
    prediction =myNN.runNN(dataSource[3][:10][::-1])[0]
    # print(prediction)
    result['nextDay']={}
    result['nextDay']['prediction']=prediction
    for i in range(24):
        dataItem=dataTrain[i]
        # print(dataTrain)
        date=dateArray[i]
        # dataTrain=dataTrain[0]
        trueValue=dataItem[1][0]
        # print(dataTrain[0])
        prediction =myNN.runNN(dataItem[0])[0]
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
        curvefile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_'+stockSymbol+'_ANN.json'
        avgFile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_averageErr_ANN.json'
    else:
        curvefile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\intraday\\prediction_'+stockSymbol+'_ANN.json'
        avgFile=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\intraday\\prediction_averageErr_ANN.json'
    # print(result)
    with open(curvefile,"w") as f:
        json.dump(result,f)

    with open(avgFile,"r") as f:
        # errStr=json.load(f)
        errDict = json.load(f)
        errDict[stockSymbol]=averageError
    with open(avgFile,"w") as f:
        json.dump(errDict,f)

    # print(dateArray)
    # print(dataTrain)
    for inputData,outputData in dataTrain:
        predictionItem=myNN.runNN(inputData)
        print(inputData,outputData,predictionItem)

def initializeWeightFile():
    keys=['AMZN','BABA','BIDU','FB','GOOGL','JD','MSFT','NVDA','TSLA','WB']
    d={}
    for key in keys:
        d[key]=[]
    # d[1]=[1,2,3]
    with open('prediction_ANNweights.json','w') as f:
        json.dump(d,f)
        # a=json.load(f)
        # print(a)

def ANNCaller(stockSymbol,isDaily=True):
    dataTrain=readJson(stockSymbol,10,isDaily)
    # print(dataTrain)
    myNN = NN(11, 5, 1)
    myNN.loadWeights(stockSymbol)

    result=[]
    resultJson={}
    resultJson[stockSymbol]={}

    prediction=[0]*4
    for i in range(4):
        # print(dataTrain[i])
        prediction[i] = round(myNN.runNN(dataTrain[i][::-1])[0],2)
    # print(dataTrain)
    stdev=round(statistics.stdev(dataTrain[3]),2)
    averageErrorPath=''
    if isDaily:
        averageErrorPath=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\daily\\prediction_averageErr_ANN.json'
    else:
        averageErrorPath=path.abspath(path.join(path.abspath(sys.argv[0]), ".."))+'\\dataset\\intraday\\prediction_averageErr_ANNA.json'

    with open(averageErrorPath,'r') as f:
        averageError=json.load(f)[stockSymbol]

    # print(prediction)

    return(prediction[0],prediction[1],prediction[2],prediction[3],averageError,stdev)


if __name__ == "__main__":
    # errorArray=[0.1,0.02][:1]
    # LRarray=[0.5,0.75,1,1.5,3,5][:1]
    # for errorRequirement in errorArray:
    #     for learningRate in LRarray:
    #         predictANN(errorRequirement,learningRate)
    keys=['AMZN','BABA','BIDU','FB','GOOGL','JD','MSFT','NVDA','TSLA','WB']
    for key in keys:
        ANNCaller(key)