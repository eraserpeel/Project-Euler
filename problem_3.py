

from math import sqrt

def is_prime(number):
	root = int(sqrt(number)) +  1
	for i in range(2, root):
		if number % i == 0:
			return False
	return True

#Brute Force Method
def brute_force_method(number):
	divide_with = 1
	while True:
		if (float(number) / divide_with).is_integer():
			if is_prime(number / divide_with):
				return number / divide_with
		divide_with += 1
	return None

#An optimized method
def optimized_method(number):
	i = 2
	while i**2 <= number:
	    if number % i == 0:
	        number = number / i
	        largest = i
	    else:
	        i += 1
	if number > largest: 
		return number
	return largest


def main():
	to_factorize = 600851475143
	print optimized_method(to_factorize)
	print brute_force_method(10000)

if __name__=="__main__":
	main()



