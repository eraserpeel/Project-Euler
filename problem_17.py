





def main():
	to_nineteen = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
	ten = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
	hundred = 7
	thousand = 8
	and_val = 3
	count = 0
	total = 0
	for num in xrange(1, 1000):
		as_str = str(num)
		if num < 1000 and num >= 100:
			total = total + to_nineteen[int(as_str[0])] + hundred
			#print to_nineteen[int(as_str[0])], hundred
			if int(as_str) % 100 < 20:
				total = total + to_nineteen[int(as_str[1:3])]
			#	print to_nineteen[int(as_str[1:3])]
			else: 
				total = total + ten[int(as_str[1])] + to_nineteen[int(as_str[2])]
			#	print ten[int(as_str[1])], to_nineteen[int(as_str[2])]
			if int(as_str) % 100 != 0:
				count += 1
				total = total + and_val
			#	print and_val
		elif num < 100 and num >= 20:
			total = total + ten[int(as_str[0])] + to_nineteen[int(as_str[1])]
			#print ten[int(as_str[0])],  to_nineteen[int(as_str[1])]
		elif num < 20:
			total = total + to_nineteen[num]
			#print to_nineteen[num]
		

		# if num < 10:
		# 	print num, as_str[0], total
		# elif num < 100:
		# 	print num, as_str[0], as_str[1], total
		# elif num < 1000:
		# 	print num, as_str[0], as_str[1], as_str[2], total
			#print to_nineteen[int(as_str[0])], 
	
	#total = total + 11 # for 1 thousand
	print total + 11
	print count



if __name__=="__main__":
	main()