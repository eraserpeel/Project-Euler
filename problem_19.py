




def main():
	months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	days = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
	date = 1
	day_of_week = "Mon"
	month = 0
	year = 1900
	add_leap = 0
	total_days = 0
	carry_over = 0
	sundays = 0
	while year != 2001:
		if year % 4 == 0:
			months[1] = 29
		else:
			months[1] = 28

		for month in months:
			day_of_week = days[(month + carry_over) % 7]
			carry_over = (month + carry_over) % 7
			if day_of_week == "Sun" and year != 1900:
				sundays += 1
		year += 1
	print sundays 


if __name__=="__main__":
	main()