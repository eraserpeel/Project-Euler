


import operator
from math import sqrt

def main():
	
	amicable = {}
	for num in range(1, 10000):
		a = sum([i for i in range(1, num / 2  + 1) if (float(num) / i).is_integer() == True])
		b = sum([i for i in range(1, a / 2  + 1) if (float(a) / i).is_integer() == True])

		#print num, a, b
		if num != a and num == b:
			print num, a, b
			if not amicable.has_key(a):
			 	amicable[a] = 0
			if not amicable.has_key(num):
			 	amicable[num] = 0
	total = 0
	for key in amicable:
	 	print key, amicable[key]
	 	total = total + key
	 	
	print total
if __name__=="__main__":
	main()