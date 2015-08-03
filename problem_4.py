


def is_palindrome(string):
	str_length = len(string) - 1
	for i in range(0, str_length):
		if string[i] != string[str_length - i]:
			return False
	return True

def main():
	max_product = 0
	for number1 in range(999, 99, -1):
		for number2 in range(number1, 99, -1):
			product_as_str = str(number1 * number2)
			if number1 * number2 > max_product:
				if is_palindrome(product_as_str):
					max_product = number1 * number2
	print max_product


if __name__=="__main__":
	main()



