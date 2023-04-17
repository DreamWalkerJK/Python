def JudgeIsPrimeNumber(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print('{0} is not prime'.format(num))
                print('{0} * {1} = {2}'.format(i, num//i, num))
                break
        else:
            print('{0} is prime'.format(num))
    else:
        print('{0} is not prime'.format(num))

a = 1
while(a >= 1):
    a = int(input("Enter the interger until you enter 1:"))
    JudgeIsPrimeNumber(a)