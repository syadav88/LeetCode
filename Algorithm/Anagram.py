def isAnagram(s1,s2):
	d = {}
	if len(s1) != len(s2):
		return False
	for i in s1:
		try:
			d[i] += 1
		except:
			d[i] = 1
	for i in s2:
		d[i] -= 1
		if d[i] < 0:
			return False
	return True

print isAnagram('sonali', 'ilanos')
print isAnagram('raashid', 'dihsar')
print isAnagram('raashid', 'dihsaar')