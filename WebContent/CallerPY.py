# written by: KangKang.Li
# assisted by: Lang.Liu
# debugged by: Jiawen.Sun Mingbo.Zhang
import sys
from PredictionBayesian import bayesianCaller
from PredictionANN import ANNCaller
import ctypes  # An included library with Python install.

def caller(stockSymbol,date,priceType):
    # y_t = np.loadtxt(filename)
    # peolpex = int(y_t[0][0])
    # peolpey = int(y_t[0][1])
    # firex = int(y_t[1][0])
    # firey = int(y_t[1][1])

    # answer = getQ(peolpex, peolpey, firex, firey)
    print(0.123)
    print(date)
    print(priceType)
    # return 'test loading py methods'


if __name__ == "__main__":
    stockSymbol= sys.argv[1]
    # date= int(sys.argv[2])
    # priceType = int(sys.argv[3])
    # caller(stockSymbol,date,priceType)
    # result=bayesianCaller(stockSymbol,date,priceType)
       
    #ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)
    result=bayesianCaller(stockSymbol)
    resultANN=ANNCaller(stockSymbol)
	
    # priceType: 0,1,2,3 for open, high, low, close
    # date for how many days ago. default value 0 for predicting next day
    # if len(result)!=3:
    #     print(-1)
    #     print(-1)
    #     print(-1)
    # print(result[0])# Predicted price
    # print(result[1])# historical error
    # print(result[2])# fluctuation range
    for item in result:
        print(item)
    for item in resultANN:
        print(item)
    