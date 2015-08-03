


term2 = 1
term1 = 2
total_sum = 0

while term1 <= 4000000:
	if term1 % 2 == 0:
		total_sum += term1
	temp_term = term1 
	term1 = term1 + term2
	term2 = temp_term
print total_sum

