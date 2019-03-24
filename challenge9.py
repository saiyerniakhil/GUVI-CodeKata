try:
    x = input().split(" ")
    n,k = int(x[0]),int(x[1])
    #print(n,x)
    n_a = [int(i) for i  in range(1,n+1)]
    sum = 0
    print(n_a)
    if(k < n):
        for i in range(0,k):
            sum = sum + n_a[i]
    else:
        print('invalid',end="")
    print(sum,end="")
except:
    print('invalid',end="")