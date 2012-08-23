import math

def primeCount(x,y=0):
	count = x

	while True:
		if y == 0:raw_input("")
		else:pass
		isprime = True

		for x in range(3,int(math.sqrt(count)+1),3):
			if count % x == 0:
				isprime = False
				break

		if isprime:
			print count

		count +=2


primeCount(input("Enter an odd number to start with: "),14)

