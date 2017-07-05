# majority element which appears more than (n/2) times for an array of size n

def majorityElement(array):
	dic = {}
	for elem in array:
		try:
			dic[elem] += 1
		except:
			dic[elem] = 1
	for key in dic.keys():
		if dic[key] > len(array)/2:
			return key
		else:
			return "No majority element present"

a1 = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5,5,5,5,5,6]
a2 = [1, 2, 3, 4, 4, 4, 4, 4]

print majorityElement(a1)

print majorityElement(a2)


l2 = [1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5,5,5,5,5,6]
l = [1, 2, 3, 4, 4, 4, 4, 4]
d = {}
for i in l:
	try:
		d[i] += 1
	except:
		d[i] = 1

print d
print len(l)

for keys in d.keys():
	if d[keys] > len(l)/2:
		print keys



