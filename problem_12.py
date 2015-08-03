
from math import sqrt
import operator

class SieveOfEratothense:

	def __init__(self, max_range):
 		self.max_range = max_range
		self.initializeSieve() 		
		self.runSieve()

 	def initializeSieve(self):
 		self.data = [i for i in range(0, self.max_range+1)]
 		self.data_length = len(self.data)
 		self.data[1] = 0
 		print "Sieve Initialized"

 	def runSieve(self):
 		index = 2
 		completed = False
 		while not completed:
			p = self.data[index]  
			self.deleteMultiples(p)
			index = self.findNextP(index)
			if index == -1:
				completed = True
		print "Sieve built"

	def getCleanSieve(self):
		return [i for i in self.data if i != 0]

	def findNextP(self, start_at):
		for i in range(start_at + 1, self.data_length):
			if self.data[i] != 0:
				return i
		return -1

 	def deleteMultiples(self, p):
 		count = 2
 		p_product = p * count
 		while p_product < self.data_length:
			self.data[p_product] = 0
			count += 1
			p_product = count * p 

	def printSieve(self):
		print self.data

	def sumOf(self):
		return reduce(operator.add, self.data)


sieve = SieveOfEratothense(10000)
prime_list = sieve.getCleanSieve()

def prime_generator():
	for prime in prime_list:
		yield prime

def triangle_number_generator(term):
	while True: 
		yield sum(range(1, term + 1))
		term += 1

def prime_factorization(number):
	factors = []
	for prime in prime_generator(): 
		while number % prime == 0:
			factors.append(prime)
			number = number / prime
	return factors

def factors_count(factors):
	to_count = list(set(factors))
	counts = []
	for i in to_count:
		counts.append(factors.count(i) + 1)
	return counts, to_count

def main():
	for num in triangle_number_generator(28): 
		prime_factors = prime_factorization(num)
		num_of_factors, tc = factors_count(prime_factors)
		if reduce(operator.mul, num_of_factors) > 500: 
			print num, prime_factors, num_of_factors, tc
			print prime_factors.count(1)
			break

if __name__=="__main__":
	main()



