x = input().split(" ")
s1,s2 = x[0],x[1]

y = s1
for i in range(len(s1)):
    y = y.replace(y[i],s2[i])

print(y)

if(y == s2):
    print("yes")
else:
    print("no")