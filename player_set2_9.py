x = int(input())

def isPrime(x):
    primes = [2,3,5,7,11,13,17,19]
    if(x in primes):
        return True
    else:
        for i in range(1,x+1):
            if(x%i == 0):
                count += 1
        if(count <= 2):
            return True
        else:
            return False

for i in range(1,x):
    if(x/i==0 and isPrime(i)):
        print(i,end=" ")

 