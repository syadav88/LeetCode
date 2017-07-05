# intersection of two arrays

'''def intersection(arr1,arr2):
	res_arr = []
	for i in arr1:
		for j in arr2:
			if i==j:
				res_arr.append(i)
				i += 1
				j += 1
	return res_arr

a1 = [1,2,2,3]
a2 = [2,2]
print intersection(a1,a2)

l1 = [1,2,3,4,5]
l2 = [2,3,4]

print intersection(l1,l2)'''


def intersection(arr1,arr2):
	dic = {}
	res = []
	for elem in arr1:
		try:
			dic[elem] += 1
		except:
			dic[elem] = 1
	for elem in arr2:
		if elem in dic and dic[elem] > 0:
			res.append(elem)
			dic[elem] -= 1
	return res

a1 = [1,2,2,1]
a2 = [2,2]

print intersection(a1,a2)

l1 = [1,2,3,4,5,6]
l2 = [2,3,4,6,6,6,6]

print intersection(l1,l2)
