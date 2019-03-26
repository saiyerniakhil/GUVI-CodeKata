try:
    x = input()
    if x.isalpha() and len(x) == 1 :
        print("Alphabet",end="")
    else:
        print('no',end="")
except:
    print('no',end="")