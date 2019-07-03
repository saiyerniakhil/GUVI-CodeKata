
try:
    x = [int(i) for i in input().split()]
    a,b = x[0],x[1]


    primes = []
    for i in range(a,b):
        count = 0
        for j in range(1,i+1):
            if(i%j == 0):
                count += 1
            else:
                continue
        if(count == 2):
            primes.append(i)

    print(len(primes))
except:
    print("enter only numbers")