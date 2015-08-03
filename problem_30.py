
import operator

def main():
	numbers = []
	for num in range(0, 1000000):
		total = reduce(operator.add, [(int(i)**5) for i in str(num)])
		if total == num:
			numbers.append(total)
	print numbers
	print sum(numbers)

if __name__=="__main__":
	main()