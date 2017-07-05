# to find a substring insiide of another string. 'in' in 'string'; return the starting index of the substring

def strStr(haystack, needle):
	for index in range(len(haystack)-len(needle) + 1):
		if haystack[index:index+len(needle)] == needle:
			return 'Yes'
	return 'No'

print strStr('Sonali', 'ona')
print strStr('String', 'in')
print strStr('string', 'sin')