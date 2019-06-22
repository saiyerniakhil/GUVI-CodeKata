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

    for i in arms:
        print(i,end="")
except:
    print("please enter integers")


