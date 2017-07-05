# missing number from the series

'''for i in range(len(a4)+1):
	if i != a4[i]:
		print i
		break'''



'''def missingNumber(arr):
	for num in range(len(a)+1):
		if num != arr[num]:
			return num'''

def missingNumber(nums):
    n = len(nums)
    return n * (n+1) / 2 - sum(nums)


a = [0,1,3]
a1 = [0,1,2,3,5]
a2 = [0,1,2,4,5]
a3 = [0,1,2,3,4,6]
a4 = [0,1,2,4,5,6]

print missingNumber(a)
print missingNumber(a1)
print missingNumber(a2)
print missingNumber(a3)
print missingNumber(a4)
