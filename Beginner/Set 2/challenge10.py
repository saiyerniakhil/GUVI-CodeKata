try:

    x = int(input())

    for i in range(1,6):
        if(i == 5):
            print(x*i,end="")
        else:
            print(x*i,end=" ")
except:
    print("please enter integers")
