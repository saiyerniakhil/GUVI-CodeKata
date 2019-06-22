x = input().split(" ")
n,q = int(x[0]), int(x[1])
try:
    for i in range(n+1,q):
        if ( i % 2 == 0):
            continue
        else:
            if not(i == q-1):
                print(i,end=" ")
            else:
                print(i,end="")
except:
    print("invalid",end="")