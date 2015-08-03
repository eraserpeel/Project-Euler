
from itertools import permutations
####
#Clean implementation

# import itertools

# js = lambda chars : int(''.join(chars))

# ans = set()
# for s in itertools.permutations('123456789', 9):
#     x,y,z = js(s[:2]),js(s[2:5]),js(s[5:])
#     i,j = js(s[:1]),js(s[1:5])
#     if x*y == z or i*j == z:
#         ans.add(z)

# print(sum(ans))


def get_int(test, lowerbound, upperbound):
	return int("".join(test[lowerbound: upperbound]))

def compute(test):
	#test 1
	if get_int(test, 0, 1) * get_int(test, 1, 5) == get_int(test, 5, 9):
		return get_int(test, 5, 9)
	elif get_int(test, 0, 2) * get_int(test, 2, 5) == get_int(test, 5, 9):
		return get_int(test, 5, 9)
	return 0

def main():
	num_set = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
	count = 0
	total = 0
	d = {}
	for perm in permutations(num_set):
		total = compute(perm)	
		if total != 0:
			d[total] = 1
		count += 1
	total = 0
	for key in d:
		print key
		total += key 
	print count, total

if __name__=="__main__":
	main()