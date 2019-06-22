x = int(input())

if x == 20 or x < 20:
    fact = 1
    for i in range(x,1,-1):
        fact *= i
    print(fact,end="")
else:
    print("enter x in range")