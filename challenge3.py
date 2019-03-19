try:
	x = input()
	x = x.lower()
	vowels = ['a','e','i','o','u']
	if len(x) == 1 and x.isalpha():
		if x in vowels :
			print('Vowels')
		elif x not in vowels and x.isalpha():
			print('Consonants',end="")
	else:
		print('Invalid',end="")
except:
	print('Invalid',end="")
