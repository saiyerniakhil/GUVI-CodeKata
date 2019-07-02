x = int(input())

roman = ''
four = 'IV'
def less_than_4(x):
    roman = ''
    roman += 'I' * x
    return roman

def between_5_and_9(x):
    roman = 'V'
    roman = roman + (x-5) * 'I'
    return roman

def between_10_and_21(x):
    roman = 'X'
    if (x-10 in range(4)):
        roman += less_than_4(x-10) 
    elif(x-10 == 4):
        roman += 'IV'
    elif(x-10 == 9):
        roman += 'IX'
    elif(x-10 in range(5,10)):
        roman += between_5_and_9(x-10)
    elif(x-10 == 10):
        roman += 'X'

    return roman

if(x in range(1,4)):
    res = less_than_4(x)
elif(x == 4):
    res = 'IV'
elif( x in range(5,8)):
    res = between_5_and_9(x)
elif( x == 9 ):
    res = 'IX'
elif(x in range(10,21)):
    res = between_10_and_21(x)


print(res,end="")


    
    

print(roman)