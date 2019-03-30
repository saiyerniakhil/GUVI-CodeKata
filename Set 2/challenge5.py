try:
    x = input().split(" ")
    n,q = int(x[0]), int(x[1])
    for i in range(n+1,q):
        if ( i % 2 == 0):
            if not(i == q-1):
                print(i,end="")
            else:
                print(i,end=" ")
        else:
            continue
except:
    print("invalid",end="")