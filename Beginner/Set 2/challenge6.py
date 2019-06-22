x = input().split(" ")

try:
	x,y = int(x[0]), int(x[1])
	primes= []

	for i in range(x,y):
			count = 0
			for j in range(1,i+1):
					if(i % j == 0):
							count += 1
			if(count == 2):
					primes.append(i)

	for i in range(0,len(primes)):
			if(i == len(primes)-1):
				print(primes[i],end="")
			else:
				print(primes[i],end=" ")
except:
	print("Please enter integers only")
