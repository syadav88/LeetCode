# Best time to buy and sell a stock II
# This quetion means that find the relative difference between consective days and if the value if positive that means it is profitable
# price(today) - price(tomorrow)>0 - sell today else tomorrow

def maxProfit(price_array):
	profit = 0
	for num in range(len(price_array)):
		profit += max(price_array[num+1]-price_array[num], 0)
	return profit

def maxProfit(priceArray):
	return sum(max(map(lambda x: x[i+1] - x[i],priceArray),0) for i in range(len(priceArray)))
