


import operator

def main():
	
	print sum([int(j) for j in str(reduce(operator.mul, [i for i in range(1, 101)]))])


if __name__=="__main__":
	main()