# Sum of two Integers

def integerSum(a,b):
	total = a
	while b != 0:
		total = a^b
		b = (a&b) << 1
		a = total
	return total

print integerSum(1,2)
print integerSum(11,2)
print integerSum(18,22)