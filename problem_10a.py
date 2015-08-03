
import operator
from math import sqrt

def is_prime(number):
	root = int(sqrt(number)) +  1
	for i in range(2, root):
		if number % i == 0:
			return False
	return True

def main():
	sum = 0
	for i in range(2, 2000000):
		if is_prime(i):
			sum += i
			#print i
		if i % 10000 == 0:
			print i
	print sum

if __name__=="__main__":
	main()



