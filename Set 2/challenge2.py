try:
    x = input()
    if (x == x[::-1]):
        print("yes",end="")
    else:
        print("no",end="")
except:
    print('invalid',end="")