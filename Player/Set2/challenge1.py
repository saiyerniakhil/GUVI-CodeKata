class Days:
    def holiday(self,x):
        holidays = ['sunday','saturday']
        if x.lower() in holidays:
            return "yes"
        else:
            return "no"

x = input().split(" ")
ob = Days()

for i in x:
    print(ob.holiday(i))

