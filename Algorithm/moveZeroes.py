# moveZeroes

def moveZeroes(array):
	for elem in array:
		if elem == 0:
			array.remove(elem)
			array.append(elem)
	return array


print moveZeroes([1,2,0,3,0,12,0,0,9])
print 
print moveZeroes([1,2,0,3,0,12,10,0,9,0,8,0])