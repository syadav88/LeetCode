'''def maxProfit(arr):
	diff = 0
	temp = 0
	for i in range(len(arr)-2):
		if a[i+1]>a[i]:
			temp = a[i+1] - a[i]
			if temp> diff:
				diff = temp
	return diff

a = [7,1,5,6,3,4]
print maxProfit(a)

a = [7,1,5,6,3,4]

diff = []
for i in range(len(a)-1,-1,-1):
	if a[i]>a[i-1]:
		diff.append(a[i]-a[i-1])

print max(diff)'''

def maxProfit(prices):
    max_profit, min_price = 0, float('inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


def maxProfit(self, prices):
    if n<=1:
        return 0
    max_profit=0
    low_price=prices[0]
    for i in range(1,len(prices)):
        low_price=min(low_price,prices[i])
        max_profit=max(max_profit, prices[i]-low_price)
    return max_profit


