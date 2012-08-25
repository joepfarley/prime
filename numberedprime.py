import math

def primeCount(x,y=0,z=1001):
	count = x
	bount = x
	while bount<z:
		if y == 0:raw_input("")
		isprime = True

		for x in range(3,int(math.sqrt(count)+1),3):
			if count % x == 0:
				isprime = False
				break

		if isprime:
			print count
			bount = bount +1
		count +=2


primeCount(input("Enter an odd number to start with: "),14)

