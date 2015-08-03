

from math import sqrt

def is_prime(number):
	root = int(sqrt(number)) +  1
	for i in range(2, root):
		if number % i == 0:
			return False
	return True

def main():
	prime_count = 0
	count = 1
	while prime_count < 10001:
		count += 1
		if is_prime(count):
			prime_count +=1
	print count
	
if __name__=="__main__":
	main()



