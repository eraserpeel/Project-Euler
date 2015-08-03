



def get_numbers():
	lines = []
	with open("problem_18.txt", 'r') as f:
		for line in f: 
			line = line.strip("\n")
			lines.append([int(i) for i in line.split(" ")])
	return lines

def process(data): 
	for row in range(len(data)-1, 0, -1):
		for item in range(0, len(data[row]) - 1):
			child1 = data[row][item] 
			child2 = data[row][item + 1]
			parent = data[row - 1][item]
			
			if child1 + parent > child2 + parent:
			 	data[row - 1][item] = child1 + parent
			else:
			 	data[row - 1][item] = child2 + parent
	return data

def main():
	lines = get_numbers()

	lines = process(lines)
	print lines[0]
		


if __name__=="__main__":
	main()