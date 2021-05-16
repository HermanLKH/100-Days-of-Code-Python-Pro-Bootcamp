# Prime checker

def prime_checker(number):
	if number > 1:
		is_prime_number = True

		for i in range(2, number):
			if number % i == 0:
				is_prime_number = False
				break
	if is_prime_number:
		print("It's a prime number.")
	else:
		print("It's not a prime number.")

n = int(input("Check this number: "))

prime_checker(number=n)