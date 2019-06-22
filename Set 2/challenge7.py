x = input()


sum = 0
for i in x:
    sum += int(i) * int(i) * int(i)
print(sum)

if(sum == int(x)):
    print("YES",end="")
else:
    print("no",end="")