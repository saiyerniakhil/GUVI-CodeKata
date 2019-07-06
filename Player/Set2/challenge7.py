def lcm(x,y):
    if(x > y):
        greater = x
    else:
        greater = y
    
    while(True):
        if((greater%x == 0) and (greater%y==0)):
            Lcm = greater
            break
        greater += 1
    return Lcm



x = input().split(" ")

print(lcm(int(x[0]),int(x[1])))


