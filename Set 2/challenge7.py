x = input()


sum = 0
for i in x:
    sum += int(i) * int(i) * int(i)

if(sum == int(x)):
    print("yes",end="")
else:
    print("no",end="")