
def camelCase(x):
    f = ''
    f += (x[0].upper())
    f += x[1:]
    return f


x = input().split()

for i in range(len(x)):
    if ( i == len(x) - 1):
        print(camelCase(x[i]),end="")
    else:
        print(camelCase(x[i]),end=" ")


