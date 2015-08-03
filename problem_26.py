


def division_cycle(denominator):
	remainders = {} 
 	dividend = 10 ** len(str(denominator))
 	divisor = denominator
 	number = 0
 	index = 1
	while True:
		quotient = dividend / divisor
		remainder = dividend % divisor
		dividend = (dividend - quotient * divisor) * 10
		#print dividend, quotient, remainder, number
		if remainders.has_key(remainder) == True:
			return len(str(number)) + len(str(denominator)) - 1
		else:
			remainders[remainder] = True
		number = number + quotient * index 
		index = index * 10

def main():
	max = 0
	max_index = 2 
	for i in range(10, 18):
		rtn = division_cycle(i)
		print rtn
		
if __name__=="__main__":
	main()