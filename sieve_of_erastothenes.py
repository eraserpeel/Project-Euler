
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
 	def runSieve(self):
 		index = 2
 		completed = False
 		while not completed:
			p = self.data[index]  
			self.deleteMultiples(p)
			index = self.findNextP(index)
			if index == -1:
				completed = True
	
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

