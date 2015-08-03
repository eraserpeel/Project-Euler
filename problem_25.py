

def main():
	prev_term = 1
	curr_term = 1
	term = 2
	while len(str(curr_term)) < 1000:
		term = term + 1
		temp = curr_term
		curr_term = curr_term + prev_term
		prev_term = temp
		
	print term
	
if __name__=="__main__":
	main()