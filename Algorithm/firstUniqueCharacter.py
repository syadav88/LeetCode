# First Unique Character

def firstUnique(string):
	dic = {}
	for char in string:
		try:
			dic[char] += 1
		except:
			dic[char] = 1
	unique = []
	for key in dic.keys():
		if dic[key] == 1:
			unique.append(string.index(key))
	return [string[min(unique)], min(unique)]


print firstUnique("leetcode")
print firstUnique("loveleetcode")
print firstUnique("raashid")


def firstUnique(s):
	return min([s.find(c) for c in s.ascii_lowercase if s.count(c) == 1] or [-1])
