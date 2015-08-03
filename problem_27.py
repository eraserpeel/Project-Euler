import sieve_of_erastothenes as se

def calc_primes(a, b, n):
	return 1


def main():
	sieve = se.SieveOfEratothense(1000)
	sieve = sieve.getCleanSieve()
	sieve_dict = {} 
	for i in sieve: 
		sieve_dict[i] = True


	max_count = 0
	max_a = 0
	max_b = 0
	for a in range(-1000, 1000):
		if a % 100 == 0:
			print a
		for b in range(-1000, 1000):
			count = 0
			if sieve_dict.has_key(b):
				for n in range(0, 1000):
					product = n*n + a*n + b
					if sieve_dict.has_key(product):
						count += 1
					else:
						break
				if count > max_count:
					max_a = a
					max_b = b
					max_count = count
	print max_a, max_b, max_count



if __name__=="__main__":
	main()