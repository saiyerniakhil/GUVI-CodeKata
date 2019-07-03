x = input()

y = ''
for i in range(0,len(x),2):
    y += x[i+1]
    y += x[i]

print(y)

