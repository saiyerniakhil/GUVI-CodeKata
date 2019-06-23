try:
    x = [int(i) for i in input().split(" ")]
    n,a,d = x[0],x[1],x[2]

    sum_ar = 0

    for i in range(n):
        sum_ar = sum_ar + (a+i*d)

    print(sum_ar)
except:
    print("please enter integers only")
