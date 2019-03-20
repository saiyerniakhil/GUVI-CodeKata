try:
	x = int(input())
	if(x%2==0):
		print('Even',end="")
	else:
		print('Odd',end="")
except:
	print('Invalid',end="")
