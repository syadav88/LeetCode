# if two stings are anagram of each other

def isAnagram(s1,s2):
	return sorted(s1) == sorted(s2)

print isAnagram("rat", "cat")

def isAnagram(s1,s2):
	if len(s1) != len(s2): return False
	dic = {}
	for char in s2:
		try:
			dic[char] += 1
		except:
			dic[char] = 1
	for char in s2:
		d[char] -= 1
		if d[char] < 0:
			return False

	return True

