def largestValue(list, most_value = None):
	if len(list) == 0:
		return most_value

	if most_value < list[0]:
		most_value = list.pop(0)
	else:
		list.pop(0)

	return largestValue(list, most_value)

print largestValue([1,2,3, 5, 7, 3, 8])