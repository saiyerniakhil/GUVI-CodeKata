n = int(input())
x = input()
vowels = ['a','e','i','o','u']

string = []

for i in x:
    if( not(i.lower() in vowels)):
        string.append(i)
x = ''.join(string)
print(x[::-1])

