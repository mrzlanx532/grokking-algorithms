def binary_search(list, item):
	low = 0
	high = len(list)-1

	i = 0

	while low <= high:

		print low
		print high
		print

		i = i + 1

		mid = (low + high)/2
		guess = list[mid]

		#print 'checked number: '+str(guess)

		if guess == item:
			return mid
		if guess > item:
			high = mid - 1
			#print 'high: ' + str(high)

		else:
			low = mid + 1
			#print 'low: ' + str(low)

	return None

my_list = range(1024)

print binary_search(my_list, 4)