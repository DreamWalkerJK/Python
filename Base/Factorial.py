def getFactorial(num):
    if num < 0:
        print("{0} < 0, Negative numbers don't have factorials".format(num))
    elif num == 0:
        print("{0} factorial is 1".format(num))
    else:
        fac = 1
        for i in range(1, num+1):
            fac = fac * i
        print("{0} factorial is {1}".format(num, fac))
    

a = 0
while(a >= 0):
    a = int(input("Enter the number until you enter -1:"))
    getFactorial(a)