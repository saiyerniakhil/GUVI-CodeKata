try:
	x=int(input())
	if(x > 0):
		print('Positive',end="")
	elif(x < 0):
		print('Negative',end="")
	else:
		print('Zero',end="")
except:
	print("Error",end="")

