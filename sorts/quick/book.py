# python2.7
# Quick sort. O(n log n)

def quickSort(array):
	if len(array) < 2: 
		return array

	pivot = array[0]

	less = [i for i in array[1:] if i <= pivot] # array[1:] - get all items without first element
	greater = [i for i in array[1:] if i > pivot]

	return quickSort(less) + [pivot] + quickSort(greater)


quickSort([10, 5, 2, 3])
