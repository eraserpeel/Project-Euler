


import operator

def get_names():
	with open("problem_22.txt", 'r') as f:
		for line in f: 
			line = line[1:-1]
			line = line.split("\",\"")
	return line
def get_alpha_value(name):
	return sum([ord(letter) - 64 for letter in name])

def main():
	names = get_names() 
	names.sort() 
	# for name in names:
	# 	print name, get_alpha_value(name)
	print sum([get_alpha_value(names[index]) * (index + 1) for index in range(0, len(names))])

	

if __name__=="__main__":
	main()