# SingleInteger

def singleInteger(array):
	dic = {}
	for i in array:
		try:
			dic[i] += 1
		except:
			dic[i] = 1
	for key in dic.keys():
		if dic[key] == 1:
			return key

lst = [1,2,3,4,5,6,7,1,2,3,4,5,6]
print singleInteger(lst)

lst2 = [1,2,3,4,5,6,7,1,2,3,4,5,7]
print singleInteger(lst2)