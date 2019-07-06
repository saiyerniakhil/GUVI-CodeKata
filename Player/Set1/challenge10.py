x = input().split(" ")

s1 = x[0]
s2 = x[1]

if(len(s1) == len(s2)):
    x = [i for i in range(len(s1)) if s1[i] != s2[i]]

# print(x)

if(len(x) == 1):
    print("yes")
else:
    print("no")