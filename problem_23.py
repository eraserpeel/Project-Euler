
from math import sqrt
import operator

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def get_abundant_numbers():
	abundant = []
	for i in range(1, 23124):
		sumfactors = sum(factors(i)) - i
		if sumfactors > i:
			abundant.append(i)
	return abundant

def get_abundant_sums(abundant):
	sum_dict = {}
	for i in abundant:
		for j in abundant:
			sum_dict[i + j] = True
	return sum_dict

						

def main():

	abundant = get_abundant_numbers()
	sum_dict = get_abundant_sums(abundant)
	#4179871

	print "Starting..."
	print sum(i for i in range(1, 23124) if sum_dict.has_key(i) == False)
		
	
if __name__=="__main__":
	main()