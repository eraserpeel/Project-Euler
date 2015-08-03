

import operator


def main():

	divisors = []
	dividend = [i for i in range(1, 21)]

	for i in range(1, len(dividend)):
		division_occurred = True
	
		while division_occurred:
			division_occurred = False
			for value in range(1, len(dividend)):
				if dividend[value] % i == 0 and i != 1 and dividend[value] != 1:
					division_occurred = True
					dividend[value] = dividend[value] / i
			if division_occurred:
				divisors.append(i)		
	print reduce(operator.mul, dividend+divisors, 1)
	
if __name__=="__main__":
	main()



