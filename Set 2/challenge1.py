try:
    x = input().split(" ")
    x = [int(i) for i in x]

    n, k = x[0],x[1]

    print(n**k,end="")
except ValueError:
    print('invalid')