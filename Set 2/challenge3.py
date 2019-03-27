try:
    x = int(input())
    i = 0
    j = 1
    while( j <= x):
        if(x % j == 0):
            i += 1
        j += 1

    if (i == 2):
        print('yes',end="")
    else:
        print('no',end="")
except ValueError:
    print('invalid',end="")