import operator

def get_numbers():
	lines = []
	with open("problem_13.txt", 'r') as f:
		for line in f: 
			lines.append(line.strip("\n"))
	return lines

def sum_big_numbers(numbers):
	summation = []
	col_sum = 0
	for col in range(len(numbers[0])-1, -1, -1):
		for row in range(0, len(numbers)):	
			col_sum += int(numbers[row][col])
		summation.append(col_sum % 10)
		col_sum = int(col_sum / 10)
	summation.reverse()
	return "".join([str(i) for i in [col_sum] + summation])

def main():
	numbers = get_numbers()
	summation = sum_big_numbers(numbers)
	print(str(summation)[:10])

if __name__=="__main__":
	main()


	# summation = reduce(operator.add, [int(i) for i in numbers])
	# print(str(summation)[:10])

