try:
    x = int(input())

    fact = 1
    for i in range(x,1,-1):
        fact *= i

    print(fact,end="")
except:
    print("please enter integers")