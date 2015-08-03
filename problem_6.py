

import operator

def power_of_2(x,y):
	return x + y**2

def main():
	print reduce(operator.add, range(1, 101))**2 - reduce(power_of_2, range(1, 101))

if __name__=="__main__":
	main()



