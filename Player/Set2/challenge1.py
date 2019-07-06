class Days:
    def holiday(self,x):
        holidays = ['sunday','saturday']
        if x.lower() in holidays:
            return "yes"
        else:
            return "no"

x = input()
y = input()
ob = Days()
print(ob.holiday(x))
print(ob.holiday(y))
