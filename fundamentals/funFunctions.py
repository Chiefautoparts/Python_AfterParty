'''def odd_even():
	for x in range(1, 2001):
		if x % 2 == 0:
			print  "Number is " + str(x) + ". This is an even number."
		else:
			print "Number is "+ str(x) + ". This is an odd number."
odd_even()'''

def multiply(arr, num):
	for x in range(0, len(arr)):
		arr *= num
	return arr

test = [2,4,6,8,22]

print multiply(test, 5)
#comeback and get to work

def layered_multiples(arr):
	print arr
	newArr = []
	for x in arr:
		value_arr = []
		for y in range(0,x):
			value_arr.append(1)
		newArr.append(value_arr)
	return newArr

x = layered_multiples(multiply([2,4,5],3))
print x