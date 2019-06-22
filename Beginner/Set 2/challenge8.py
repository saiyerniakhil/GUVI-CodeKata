try:
    x,y = input().split(" ")
    a,b = int(x),int(y)
    arms = []
    for i in range(a,b):
        sum = 0
        for j in str(i):
            sum += int(j) * int(j) * int(j)

        if(sum == int(i)):
            arms.append(i)
        else:
            pass


    for i in range(len(arms)):
        if(i == len(arms)-1):
            print(arms[i],end="")
        else:
            print(arms[i],end=" ")

        
except:
    print("please enter integers")


