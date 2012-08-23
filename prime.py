import math

def main():
	count = 9999999999

	while True:
		isprime = True

		for x in range(3,int(math.sqrt(count)+1),3):
			if count % x == 0:
				isprime = False
				break

		if isprime:
			print count

		count +=2

main()
