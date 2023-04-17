def getFibonacci(itemNum):
    n1 = 0
    n2 = 1
    count = 2

    if itemNum <= 0:
        print("Please enter an integer greater than 0")
    elif itemNum == 1:
        print("Fibonacci: {0}".format(n1))
    else:
        print("Fibonacci: {0},{1}".format(n1,n2), end=',')
        while count < itemNum:
            n3 = n1 + n2
            print(n3, end=',')
            n1 = n2
            n2 = n3
            count += 1
        print()

# 递归
def getFibonacciByRecursion(itemNum):
    if itemNum <= 1:
        return itemNum
    else:
        return (getFibonacciByRecursion(itemNum-1) + getFibonacciByRecursion(itemNum-2))

a = 1
while(a > 0):
    a = int(input("Enter the interger until you enter 0:"))
    if a <= 0:
        break
    # getFibonacci(a)
    for i in range(a):
        print(getFibonacciByRecursion(i))
    