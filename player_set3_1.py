import sys

x = sys.stdin.readlines()

x = [i.strip("\n").split(" ") for i in x]

#print(x)
if (x[0][0] == x[1][0] == x[2][0]):
    print("yes")
elif (x[0][1] == x[1][1] == x[2][1]):
    print("yes")
else:
    print("no")