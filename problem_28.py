


def main():
	row1 = row2 = row3 = row4 = 1
	total = 0
	counter = 2
	c = 1
	for i in range(1, 501):
		row1 += counter
		row2 += counter + 2
		row3 += counter + 4
		row4 += counter + 6
		total += row1 + row2 + row3 + row4
		counter = counter + 8
		#print row1, row2, row3, row4
		c = c + 2
		
	print c
	
	print total + 1




if __name__=="__main__":
	main()