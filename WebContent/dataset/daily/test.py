import json
# with open('AMZN.json', 'r') as f:
#     data = json.load(f)
# print(data['Meta Data'])
# print(len(data['Time Series (Daily)']))
# print(data['Time Series (Daily)']['2017-10-05'])
# print(data)
# print(len(data['Time Series (Daily)']))
# for item in data[:100]:
	# print(item)
# avgFile='prediction_averageErr_ANN.json'
# with open(avgFile,"r") as f:
#     # errStr=json.load(f)
#     errDict = json.load(f)
#     for key in errDict:
#     	errDict[key]=0
# with open(avgFile,"w") as f:
#     json.dump(errDict,f)

keys=['AMZN','BABA','BIDU','FB','GOOGL','JD','MSFT','NVDA','TSLA','WB']
d={}
for key in keys:
	d[key]=[]
# d[1]=[1,2,3]
with open('prediction_ANNweights.json','w') as f:
	json.dump(d,f)
    # a=json.load(f)
    # print(a)