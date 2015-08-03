
import numpy

#Brute Force Approach (takes too long)
def searchGrid(x, y):
	num1 = 3
	num2 = 4
	if x == num1 and y == num2:
		return 1
	total = 0
	if x < num1:
		total += searchGrid(x + 1, y)
	if y < num2: 
		total += searchGrid(x, y + 1)
	return total


def createGrid(dimension):
	grid = [[0 for x in xrange(dimension)] for x in xrange(dimension)] 
	for i in xrange(2, dimension + 2):
		grid[0][i - 2] = i
		grid[i - 2][0] = i
	for i in range(1, dimension):
		for j in range(1, dimension):
	  		grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
	print grid[19][19]
def main():
	#print searchGrid(0, 0)
	createGrid(20)


if __name__=="__main__":
	main()