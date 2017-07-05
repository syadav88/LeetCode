# ReverseString

def reverse(string):
	return string[::-1]

def reverse(string):
	newString = ''
	for num in range(len(string)-1, -1,-1):
		newString += string[num]
	return newString

print reverse("sonali")

print reverse("raashid")

print reverse("raashid&sonali")


def reverse(string):
	lastIndex = len(string)-1
	newString = ''
	for num in range(len(string)):
		while lastIndex > -1:
			newString += string[lastIndex]
			lastIndex -= 1
	return newString

print reverse("sexy")


