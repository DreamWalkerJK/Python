def JuageIsArmstrongNumber(num):
    sum = 0
    n = len(str(num))

    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** n
        temp //= 10

    if sum == num:
        print("{0} is armstrong number".format(num))
    else:
        print("{0} is not armstrong number".format(num))


a = 1
while(a > 0):
    a = int(input("Enter the interger until you enter 0:"))
    JuageIsArmstrongNumber(a)