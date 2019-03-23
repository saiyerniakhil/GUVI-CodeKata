try:
    l = input().split(" ")
    x = [int(i) for i in l]
    print(max(x),end="")
except:
    print('Invalid',end="")
