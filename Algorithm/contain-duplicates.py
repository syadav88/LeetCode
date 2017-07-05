def containDuplicates(array):
	dic = {}
	for elem in array:
		try:
			dic[elem] += 1
		except:
			dic[elem] = 1
	for key in dic.keys():
		if dic[key] > 1:
			return True
	return False

test = [1,2,3,4,5,6,7,7,8,9]
test2 = [1,2,3,4,5,6,7,8,9,0]

print containDuplicates(test2)
print containDuplicates(test)