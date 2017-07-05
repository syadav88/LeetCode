# FizzBuzz
'''
def fizzBuzz(n):
	for i in range(1,n+1):
		if i%3 ==0 and i%5 == 0:
			print 'FizzBuzz'
		elif i%3 ==0:
			print 'Fizz'
		elif i%5 == 0:
			print 'Buzz'
		else:
			print i

print fizzBuzz(15)'''


'''def FizzBuzz(n):
	return ('Fizz'*(not i%3) + 'Buzz'*(not i%5) or str(i) for i in range(1,n+1))

print FizzBuzz(15)'''


def fizzBuzz(n):
	return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]

print fizzBuzz(15)