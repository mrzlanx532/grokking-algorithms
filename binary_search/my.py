def binary_search(searchedNumber, list):

	minIndex = 0
	maxIndex = len(list) - 1

	while minIndex <= maxIndex:

		middleIndex = (minIndex + maxIndex)/2

		valueFromMiddleOfList = list[middleIndex]

		if valueFromMiddleOfList == searchedNumber:
			return searchedNumber

		if valueFromMiddleOfList < searchedNumber:
			minIndex = middleIndex + 1 
			
		if valueFromMiddleOfList > searchedNumber:
			maxIndex = middleIndex - 1

	return None
		

someArray = [1, 2, 4, 5, 6]

print binary_search(5, someArray)
