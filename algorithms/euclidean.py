# python 2.7

import sys

def mostMininalSize(firstSide, secondSide):

	longestSide = (secondSide, firstSide)[firstSide <= secondSide]
	shorterSide = (firstSide, secondSide)[firstSide <= secondSide]

	remainder = longestSide % shorterSide

	if remainder == 0:
		print str(shorterSide) + 'x' + str(shorterSide);
	else: 
		shorterSide = shorterSide - remainder;

		mostMininalSize(longestSide, shorterSide)


mostMininalSize(1680, 640)
mostMininalSize(3746, 234)
mostMininalSize(4980, 50)