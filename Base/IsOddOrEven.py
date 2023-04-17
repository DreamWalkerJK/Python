def JudgeIsOddOrEven(num):
    if (num % 2) == 0:
        print('{0} is even'.format(num))
    else:
        print('{0} is odd'.format(num))

a = 0
while(a != -1):
    a = float(input("Enter the number until you enter -1:"))
    JudgeIsOddOrEven(a)