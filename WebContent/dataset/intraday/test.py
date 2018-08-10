import json
with open('AMZN.json', 'r') as f:
    data = json.load(f)
# print(data['Meta Data'])
# print(len(data['Time Series (Daily)']))
# print(data['Time Series (Daily)']['2017-10-05'])
print(data)
# print(len(data['Time Series (Daily)']))
# for item in data[:100]:
	# print(item)