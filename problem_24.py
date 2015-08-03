
import itertools

def main():
	a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	perm_iter = itertools.permutations(a)
	lst = []
	for i in perm_iter:
		lst.append("".join(str(i) for i in list(i)))
		
	lst.sort()
	print lst[999999]
if __name__=="__main__":
	main()