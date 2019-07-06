x = [int(i) for i in input().split(" ")]
n,k = x[0],x[1]

x = [int(i) for i in input().split(" ")]
y = x[::-1]


res = []
res = y[k:] + y[:k]

res = res[::-1]
for i in range(len(res)):
    if(i == len(res) -1):
        print(res[i],end="")
    else:
        print(res[i],end=" ")
    