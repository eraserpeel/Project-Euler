
#Simple solution
total_sum = 0
for number in range(3, 1000):
	if number % 3 == 0 or number % 5 == 0:
		total_sum += number
print total_sum

#More pythonic way
print sum([i for i in range(3, 1000) if i % 3 == 0 or i % 5 == 0])