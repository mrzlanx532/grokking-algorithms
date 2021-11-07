def sum(list, acc = 0):

	if len(list) == 0:
		return acc

	acc = acc + list.pop(0)

	return sum(list, acc)


print sum([1, 2, 4, 7])